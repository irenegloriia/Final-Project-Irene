import csv
from nltk.util import pr
from numpy import testing
import pandas as pd
import requests, json
import nltk
import re
import string
from nltk.tokenize import word_tokenize
import pickle
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import csv
import math
from scipy.sparse import dok
from nltk.tag import CRFTagger
import pycrfsuite

def tfidf(teks):

    ct = CRFTagger()
    ct.set_model_file("all_indo_man_tag_corpus_model.crf.tagger")

    testingfix = [teks]

    d ={}
    j = 0
    for i in testingfix:
        i = str(i).split()
        #print("N-gram tagger")
        postag = ct.tag_sents([i])
        postag = postag[0]
        #print (postag)
        dictcorpus=dict(postag)
        d[j] = {}
        d[j]=dictcorpus
        j+=1

    #TF
    benci=[]
    bencinew=[]
    with open('unigram-irene2.csv') as csvfile:
        readCSV = csv.reader(csvfile)
        for i in readCSV:
            benci.insert(len(benci),i)

    for i in benci:
        for j in i :
            bencinew.append(j)
    worddict= dict.fromkeys(bencinew, 0)
    k=0
    dictbenci={}
    for i in d: 
        dictbenci[k]={}
        dictbenci[k]=worddict
        k+=1
    dictbencinew={}
    l=0
    for x in d.keys():
        dictbenci[x]=dict.fromkeys(dictbenci[x],0)
        for y in d[x].keys():       
            for word in bencinew:
                if(y == word):
                    dictbenci[x][word]+=1
            dictbencinew[l]={}
            dictbencinew[l]=dictbenci[x]
        l+=1
    for x in d.keys():
        for y in d[x].keys():
            for word in bencinew:    
                if(y in word and (d[x][y] == 'NN' or d[x][y] =='NNP' or d[x][y]=='NNG' or d[x][y]=='VBI' or d[x][y]=='VBT')):
                    dictbencinew[x][word]=dictbencinew[x][word]*7
                elif(y in word and (d[x][y] == 'JJ' or d[x][y]=='RB')):
                    dictbencinew[x][word]=dictbencinew[x][word]*3
                else :
                    dictbencinew[x][word]=dictbencinew[x][word]*1
    jumlahdictbenci=0
    dictbencitf={}
    z=0
    for x in dictbencinew.keys():
        for y in dictbencinew[x].keys():
            jumlahdictbenci=jumlahdictbenci+dictbencinew[x][y]
            dictbencitf[z]={}
        dictbencitf[z]=jumlahdictbenci
        z+=1
        jumlahdictbenci=0

    for x in dictbencinew.keys():
        for y in dictbencinew[x].keys():
            if(dictbencinew[x][y]>0):
                dictbencinew[x][y]=dictbencinew[x][y]/dictbencitf[x]

    #IDF
    dictidf=dict.fromkeys(bencinew,0)
    N = len(testingfix)
    for x in d.keys():
        for y in d[x].keys():       
            for word in bencinew:
                if(y == word):
                    dictidf[word]+=1
    for x in dictidf.keys():
        dictidf[x]=1 + math.log10((1+N)/(1+dictidf[x]))
    for x in dictbencinew.keys():
        for y in dictbencinew[x].keys():
            dictbencinew[x][y]=dictbencinew[x][y]*dictidf[y]
            
    #Normalisasi
    jumlahnorm=0
    dictnorm={}
    e=0
    for x in dictbencinew.keys():
        for y in dictbencinew[x].keys():
            jumlahnorm=jumlahnorm+(dictbencinew[x][y]*dictbencinew[x][y])
            dictnorm[e]={}
        dictnorm[e]=math.sqrt(jumlahnorm)
        e+=1
        jumlahnorm=0
    for x in dictbencinew.keys():
        for y in dictbencinew[x].keys():
            if(dictbencinew[x][y]>0):
                dictbencinew[x][y]=dictbencinew[x][y]/dictnorm[x]
        
    df = pd.DataFrame.from_dict(dictbencinew, orient='index')
    dictio = df.to_dict()
    dict2 = {}
    for key in dictio:
        if(dictio[key][0]>0):
            dict2[key] = dictio[key][0] 
    print("dict2",dict2)
    predict=df.values.tolist()
    print("predict",predict)
    return predict[0],dict2

