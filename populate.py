from sqldb import *
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
from binarytree import Node, pprint ,convert
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import re

file = 'Sports_sentences.xlsx'

xl = pd.ExcelFile(file)

df1 = xl.parse('Sheet1')

k=0
for i in df1['SENTENCES']:
    s=re.sub('[^ a-zA-Z0-9]', ' ', i)
    flag1=0
    O_sent=s
    word_list=word_tokenize(O_sent)
    stop = set(stopwords.words('english'))
    operator=set(('i'))
    stopWords=set(stop)-operator
    stopWords.update(('.',',','?','!','/','-','_'))
    wordsFiltered = []
    for w in word_list:
        if w not in stopWords:
            wordsFiltered.append(w)

    dict1=nltk.pos_tag(word_list)
    dict2=nltk.pos_tag(wordsFiltered)

    verb=[x[0] for x in dict1 if('VB' in x[1])]

    for i in dict2:
        if(find_db(i[0],i[1])):
            update_db(i[0],i[1])
        else:
            flag1=1
            insert_db(i[0],i[1])
            
    print(s)
    
    



