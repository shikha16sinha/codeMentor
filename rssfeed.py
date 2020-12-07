import sys
import feedparser

NewsFeed = feedparser.parse("https://timesofindia.indiatimes.com/rssfeedstopstories.cms")

descp = NewsFeed.feed.subtitle
entry=NewsFeed.feed.title_detail.value
link = NewsFeed.feed.links[0].href
print entry
print descp
print link
