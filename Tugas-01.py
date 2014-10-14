#RSS Feed Parser untuk detik.com
#Diperlukan library feedparser : https://pypi.python.org/pypi/feedparser
#18210012 & 18209036 
#Tugas Protif 01
#Referensi :
#http://www.pythonforbeginners.com/feedparser/using-feedparser-in-python

import feedparser
detikfeed = feedparser.parse('http://detik.feedsportal.com/c/33613/f/656082/index.rss')
print detikfeed['feed']['title']
print detikfeed['feed']['link']
for post in detikfeed.entries:
    print post.title + ": " + post.link + "\n"
