import pandas as pd

a = pd.read_csv('DATABARUIDF.csv')
b = a[a['outcome']=='positif']