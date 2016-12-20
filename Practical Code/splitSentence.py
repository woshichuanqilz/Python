import nltk.data

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
fp = open("test.txt")
data = fp.read()
print (tokenizer.tokenize(data))
# print '\n-----\n'.join(tokenizer.tokenize(data))
