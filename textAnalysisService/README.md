# Producer and Consumer

`articleParser.py` is a kafka event consumer waiting for new events from the rss feed service.

`rssProducer.py` is a kafka event producer that runs on a cron job weekly, producing new "news events" onto the event stream. This can be configured to consume from different news services (CNN, HuffPost, Fox News)

The main advantage of theses services is they can be run in a docker container on any scalable service.
