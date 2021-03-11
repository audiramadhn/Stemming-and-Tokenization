#!/usr/bin/env python
# coding: utf-8

# Sastrawi Stemmer

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import pandas as pd

factorystem = StemmerFactory()
stemmer = factorystem.create_stemmer()
factorystop = StopWordRemoverFactory()
stopword = factorystop.create_stop_word_remover()
word_count = {}

gojek = pd.read_excel("Folder python/ulasan_gojek(1).xlsx")
sentence = pd.DataFrame.to_string(gojek) 

stop = stopword.remove(sentence)
output   = stemmer.stem(stop)
print("Kalimat:")
print(output)
print("")
print("Tokenisasi:")

words = output.split()
for word in words:
    count = word_count.get(word,0)
    count += 1
    word_count[word] = count
    
word_count_list = sorted(word_count, key=word_count.get, reverse = True)
for word in word_count_list[:100]:
    print(word, word_count[word])


# In[39]: Porter Stemmer


from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords 
import re
import pandas as pd

porter=PorterStemmer()
stops = set(stopwords.words('english')) 
word_count={}   

gojek = pd.read_excel("Folder python/ulasan_gojek(1).xlsx")
sentence = pd.DataFrame.to_string(gojek)

def stemSentence(sentence):
    sentence = re.sub(r'[^\w\s]','',sentence) 
    token_words=word_tokenize(sentence)
    stem_sentence=[]
    for word in token_words:
        stem_sentence.append(porter.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)
outputeng=stemSentence(sentence)
print("Kalimat:")
print(outputeng)
print("")
print("Tokenisasi:")

words = outputeng.split()
for word in words:
    count = word_count.get(word,0)
    count += 1
    word_count[word] = count
    
word_count_list = sorted(word_count, key=word_count.get, reverse = True)
for word in word_count_list[:100]:
    print(word, word_count[word])


# In[40]:


from nltk.tokenize import word_tokenize

text = "we were totally charmed by the hotel. a unique place, a magical atmosphere that invite relax and relax! a real change of scenery! we were impressed by the architecture of the hotel and its total integration with nature."
text_tokens = word_tokenize(text)

tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]

filtered_sentence = (" ").join(tokens_without_sw)
print(filtered_sentence)






