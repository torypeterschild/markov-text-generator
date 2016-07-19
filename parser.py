from textblob import TextBlob
import random


EOS = ['.', '?', '!']




with open('static/corpus000.txt') as f:
    content = f.read()

blob = TextBlob(content.decode('utf-8'))

for sentence in blob.sentences:
    print(sentence)

print(blob.ngrams(n=3))