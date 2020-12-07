import sys
import feedparser

NewsFeed = feedparser.parse(str(sys.argv[1]))

descp = NewsFeed.feed.subtitle
entry=NewsFeed.feed.title_detail.value
link = NewsFeed.feed.links[0].href
print entry
print descp
print link
