
import feedparser
from newspaper import Article
from time import sleep
from json import dumps
from kafka import KafkaProducer


class FeedParser():
    # Fetches rss feeds, scrapes url, title, and link
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],
            value_serializer=lambda x: dumps(x).encode('utf-8')
        )

    def parseUrl(self,url):
        print('fetching {}'.format(url))
        feed = feedparser.parse(url)
        for entry in feed.entries:
            print(' sending {}'.format(entry.title))
            data = {'title':entry.title,
                    'link':entry.link}
            self.producer.send('topic_test',value=data)
            sleep(2)
        pass

if __name__ == "__main__":
    fp = FeedParser()
    url =  "http://rss.cnn.com/rss/cnn_topstories.rss"
    fp.parseUrl(url)


'''
fp = FeedParser()
url =  "http://rss.cnn.com/rss/cnn_topstories.rss"
fp.parseUrl(url)

'''

