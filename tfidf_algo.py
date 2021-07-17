from operator import pos
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def tfidf_knn(teks):
    a = pd.read_csv('NEWDATA.csv')
    a.dropna(subset=["Normal"],inplace=True)
    vectorizer = TfidfVectorizer(use_idf=True)
    X = vectorizer.fit_transform(a['Normal'])
    y = a['Status']

    knn = KNeighborsClassifier(n_neighbors=15,metric='euclidean', p=2)   #Create KNN Classifier 
    knn.fit(X,y) #fit the classifier to the data
    
    teks = vectorizer.transform([teks])
    prediction = knn.predict(teks)
    print(prediction)
    return(prediction)