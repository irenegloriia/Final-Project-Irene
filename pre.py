import pandas as pd
import re
import string as st
import numpy as np
import nltk

# import word_tokenize & FreqDist from NLTK
from nltk.tokenize import word_tokenize 
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.tag import CRFTagger

def preprocessing(teks):
    asli = teks
    # lowercase
    teks = asli.lower()

    # remove punctuation
    def remove_punct(text):
        text = str(text)
        return text.translate(str.maketrans(st.punctuation,"                                "))
    teks = remove_punct(teks)

    # remove emdash
    def remove_spesial_punct(text):
        text = re.sub('\â€”',' ',text)
        return re.sub(r"\u2014","",text)
    teks = remove_spesial_punct(teks)

    # remove number
    def remove_number(text):
        return  re.sub(r"\d+","", text)
    teks = remove_number(teks)

    #remove spesial stopwords
    def spesial_stopword(text):
        blacklist = ["â€“","–","rp"]
        for word in blacklist:
            text = text.replace(word, '')
        return text
    teks = spesial_stopword(teks)

    #remove single char 
    def remove_singl_char(text):
        return re.sub(r"\b[a-zA-Z]\b","", text)
    teks = remove_singl_char(teks)

    #remove multiple whitespace into single whitespace
    def remove_whitespace_multiple(text):
        return re.sub('\s+',' ',text)
    teks = remove_whitespace_multiple(teks)

    #remove whitespace leading & trailing
    def remove_whitespace_LT(text):
        return text.replace('\\t'," ").replace('\\n'," ").replace('\\u'," ").replace('\\'," ")
    teks = remove_whitespace_LT(teks)
    
    blacklist = pd.read_excel('customStopwords.xlsx')
    newlist = []
    for index, row in blacklist.iterrows():
        newlist.append(row[0])
    
    # Tokenization
    def word_tokenize_wrapper(text):
        return word_tokenize(text)
    teks = word_tokenize_wrapper(teks)

    print('Setelah tokenasi : ',teks)
    print(type(teks))

    #Removal Stopwords Indonesia
    list_stopwords = set(stopwords.words('indonesian'))
    hapus = ["naik","tidak","jangan","kurang","belum","bukan","tinggi"]
    for a in hapus:
        list_stopwords.remove(a)
    list_stopwords = list_stopwords.union(newlist)

    def remove_stopwords(text):
        tokens_without_stopword = [word for word in text if not word in list_stopwords]
        return tokens_without_stopword
    teks = remove_stopwords(teks)

    # print('Setelah remove_stopwords : ',teks)
    # print(type(teks))

    #Removal Stopwords English
    from nltk import PorterStemmer
    def english_stopwords(text):
        return [word for word in text if word not in nltk.corpus.stopwords.words('english')]
    teks = english_stopwords(teks)
    
    # print('Setelah english_stopwords : ',teks)
    # print(type(teks))

    factory = StemmerFactory()
    stemmer = factory.create_stemmer()

    def stem(text):
        output = [stemmer.stem(token) for token in text]
        return output
    teks = stem(teks)

    kata_negasi = ["tidak", "jangan", "belum", "bukan","kurang"]
    def negasi(text):
        for idx, kata in enumerate(text):
            if(kata in kata_negasi):
                if(idx != len(text)-1):
                    text[idx] = text[idx]+"_"+text[idx+1]
                    text.pop(idx+1)
        return text
    teks = negasi(teks)

    def gabung(text):
        gab = " ".join(text)
        return gab
    
    teks = gabung(teks)

    return teks

