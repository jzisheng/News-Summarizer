# News Summarizer Project

Website that scrapes and summarizes major news sources.
You can view the [website here](http://142.93.119.27:5000/)



My hope is that this can be a platform where you don't have to worry about scraping or crawling web sites,
instead you just consume events from a stream, so you can focus on trying to add new features

# Documentation (WIP)
To be added

# System Design

Below is a image of high level service 
architecture

The latest articles are read 
from RSS feed subscriptions, and then
the article and its metadata is published 
onto an Kafka event stream. The motivation for
this is to be able to pull the freshest news. 
After publishing a text analytics service pulls 
the article, and performs its analysis. 
After finishing its analysis the text analytics
will insert this information into mongodb, where
the webservice can read from. 

Next steps include exploring taking advantage
of Faust, a asynchronous package for consuming
Kafka events. 

![System Design](https://github.com/jzisheng/News-Summarizer/blob/master/images/systemDesign.png?raw=true)



