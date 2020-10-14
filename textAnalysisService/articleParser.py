from transformers import AutoTokenizer, AutoModel,pipeline
from newspaper import Article
from kafka import KafkaConsumer,KafkaProducer
from json import loads, dumps
from time import sleep
import pymongo
from markdown2 import Markdown

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["blog"]
collection = db["articles"]

def createAndInsertDoc(summData):
    markdowner = Markdown()
    sanitizedHtml = markdowner.convert(summData["markdown"])
    doc = {
        "title":summData["title"],
        "description": summData["description"],
        "markdown": summData["markdown"],
        "sanitizedHtml": sanitizedHtml
    }
    collection.insert([doc])
    pass

# createDoc("Python article","this is a description","*boo!*")

class ArticleService():
    # consumes links from Kafka, and web crals to
    # transforms them into text for text service
    def __init__(self):        
        self.consumer = KafkaConsumer(
            'topic_test',
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='my-group-id',
            value_deserializer=lambda x: loads(x.decode('utf-8'))
        )
        
        self.producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],
            value_serializer=lambda x: dumps(x).encode('utf-8')
        )
        
        self.classifier = pipeline('summarization')
        self.classifierSA = pipeline('sentiment-analysis')
        print("article service")
        
    def summarizer(self,text):
        try:
            fullText = text.strip()
            if len(fullText) >= 1024:
                tokens = fullText[:1024]
            else:
                tokens = fullText
            sa = self.classifierSA(tokens)
            # print(sa['label']))
            res = self.classifier(tokens, min_length=5, max_length=100)
            return res,sa
        except IndexError:
            print("Index error")

    def parseArticleEvent(self,data):
        url, title = data["link"], data["title"]
        # get full article and run analytics
        article = Article(url)
        article.download()
        article.parse()
        if len(article.text) < 1000:
            return None
        # analyze and publish data
        article.nlp()
        keywords = article.keywords[:3]
        summ,sa = self.summarizer(article.text)
        summ = summ[0]["summary_text"]
        sa = sa[0]
        summData = {'title':title,'url':url,
                    'description':summ,
                    'markdown':article.text,
                    'label':sa['label'],
                    'score':sa['score']}
        return summData
    
    def fetchText(self):
        print("="*10)
        print('fetching text..')
        print("="*10)        
        for event in self.consumer:
            event_data = event
            if "link" in event_data.value:
                # Parse rss feed
                data = event_data.value
                summData = self.parseArticleEvent(data)
                if summData != None:
                    print("Parsed {}".format(summData['title']))
                    self.producer.send('topic_summ', value=summData)
                    createAndInsertDoc(summData)
            else:
                continue
            sleep(1)
            pass
        pass


if __name__ == "__main__":
    a = ArticleService()
    a.fetchText()


