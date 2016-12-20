import webarticle2text
import sys

with open('HOCTranscriptURL.txt') as f:
    urllist = f.read().splitlines()
for url in urllist:
    filename = url.split("=")[-1]
    filename = "./Transcript/HOC_" + filename + ".txt"
    article = webarticle2text.extractFromURL(url)
    with open(filename, 'a') as the_file:
        the_file.write(article)
    print filename + " written!"

