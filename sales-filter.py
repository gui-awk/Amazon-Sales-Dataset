import numpy as np 
import pandas as pd 
import os

df = pd.read_csv('amazon.csv') 

df.columns #checking

#df.info() #checking

#df.describe() #checking

df = df.dropna() #handling NaN  values

df.isnull().sum() #sum null values


#processing rating count
for i in df['rating_count'].values:
    print(i,'|',int(i.replace(',',''))) #print rating count values with | and replacing , for better visualization 
    break

rating_count = []  #creating a rating count list to put i values inside the list
for i in df['rating_count'].values:
    rating_count.append(int(i.replace(',','')))

df['rating_count'] = rating_count


filter_rating_count = df.query('rating_count <= 24269').sort_values(by=['rating_count'], ascending=True) #first time using sort_values

filter_rating_count.head()


#same process in discounted_price

for i in df['discounted_price'].values:
    print(i,'|',float(i[1:].replace(',',''))) #IndexError: invalid index to scalar variable.
    break

discounted_price = []
for i in df['discounted_price'].values:
    discounted_price.append(float(i[1:].replace(',',''))) #float for ,

df['discounted_price'] = discounted_price

filter_discounted_price = df.query('discounted_price >= 300')
filter_discounted_price.head()

#unique category

unique_category = []

for i in df['category'].values:
    unique_category += i.split('|')


unique_category = list(set(unique_category))

#quantidade       

data = []
for i in unique_category:
    c = 0
    for j in df.values:
        if(i in j[2]):
            c += 1
    data.append([i, c])  # [[Categoria, quantidade de produtos na categoria]]

#sort

df_pr = pd.DataFrame(data, columns=['category', 'frequency'])
df_pr.sort_values(by='frequency', ascending=False)