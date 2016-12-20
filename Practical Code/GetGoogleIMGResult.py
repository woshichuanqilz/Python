import urllib2
import simplejson
import cStringIO
import lizhexxx
import sys

sys.stderr = open('errorlog.txt', 'w')

fetcher = urllib2.build_opener()
searchTerm = 'parrot'
startIndex = 0
searchUrl = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + searchTerm + "&start=" + startIndex
f = fetcher.open(searchUrl)
deserialized_output = simplejson.load(f)

sys.stderr.close()
sys.stderr = sys.__stderr__
