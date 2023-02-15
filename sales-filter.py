import numpy as np 
import pandas as pd 
import os

df = pd.read_csv('amazon.csv')

df.columns

#df.info()

#df.describe()

df = df.dropna()

df.isnull().sum()


#processando rating count
for i in df['rating_count'].values:
    print(i,'|',int(i.replace(',','')))
    break

rating_count = []
for i in df['rating_count'].values:
    rating_count.append(int(i.replace(',','')))

df['rating_count'] = rating_count

#df.head()

filtrando = df.query('rating_count >= 24269')
print(filtrando)
filtrando.head()

