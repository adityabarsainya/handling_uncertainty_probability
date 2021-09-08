import time
from sqldb import *
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
from binarytree import Node, pprint ,convert

def tree(t_sent,arr):    
    arr1=[]
    C_sent=t_sent
    root = Node(t_sent)
    temp=root
    for x in arr:
        arr1=C_sent.split(x)
        temp.left=Node(arr1[0])
        temp.right=Node(arr1[1])
        temp=temp.right
        C_sent=arr1[1]
    pprint(root)

def parseTree(temp):
    
    grammar =r"""
     NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
     PP: {<IN><NP>}               # Chunk prepositions followed by NP
     VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
     CLAUSE: {<NP><VP>}           # Chunk NP, VP
     """
    cp = nltk.RegexpParser(grammar)
    result = cp.parse(temp)
#    print(result)
    result.draw()


print("----- I'm a new learning agent. I might interpret your command wrong initially but I'll promise you I'll learn. -----")
print("\t--- I'll give you the right way of parsing a sentence and that's how i interpret your order ---\n")
#O_sent=" you there?"
while(1):
    start=time.time()
    flag1=0
    O_sent=input("How may i help you?\n--> ")
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

    print("Words: ",dict1)
    print("Words: ",dict2)

    verb=[x[0] for x in dict1 if('VB' in x[1])]
    print("Verb: ",verb)
    tree(O_sent,verb)

    parseTree(dict1)

    print("\n\nI might end up tagging words in the wrong way but hey, I can correct them. Just give me a push!\n")
    for i in dict2:
        if(find_db(i[0],i[1])):
            update_db(i[0],i[1])
        else:
            flag1=1
            insert_db(i[0],i[1])
    show_db()

    dict3=[]
    l=[]
    print("I'm sorry if there's a mistake. This is my Knowledge base. You can help me learn. ")
    for i in dict1:
        l.append(list(i))
    for j in dict2:
        for i in l:
            if(i[0]==j[0]):
                i[1]=correctPos_db(i[0])
            
    if(flag1==0):
        for i in l:
            dict3.append(tuple(i))
        parseTree(dict3)
        #take=input("Do you want to quit? (y/n)")
        #if(take=='y' or take=='Y'):
         #   break
    else:
        print("\nOops. I think I've encountered a new word!! Retype so that I update.\n")

    end=time.time()
    print("Time taken is: ",(end-start))
    break
    



