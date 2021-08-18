from operator import pos
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def knn(teks):
    df = pd.read_csv('TfIdfDataset6.csv', index_col = 0)
    label = pd.read_csv('DatasetPreprocessing.csv')
    label.dropna(inplace=True)
    label = label["Status"]

    knn = KNeighborsClassifier(n_neighbors=25,metric='euclidean', p=2)
    knn.fit(df,label)

    hasil = knn.predict(teks)
    return hasil