import webarticle2text
import sys
# print webarticle2text.extractFromURL("http://sanguoshaenglish.blogspot.com/2010/07/liu-bei.html")
article = webarticle2text.extractFromURL(sys.argv[1])
