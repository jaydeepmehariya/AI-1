import numpy as np
import pandas as pd

credits_df = pd.read_csv("credits.csv")
movies_df = pd.read_csv("movies.csv")
credits_df

movies_df

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

credits_df
movies_df

credits_df.head()
movies_df.tail()

movies_df = movies_df.merge(credits_df, on ='title')
movies_df.shape
movies_df.head()
movies_df.info()

movies_df = movies_df[['movie_id','title','overview','genres','keywords','cast','crew']]

movies_df
movies_df.info()
movies_df.isnull().sum()
movies_df.dropna(inplace = True)
movies_df.duplicated().sum()
movies_df.iloc[0].genres


import ast
def convert(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L


movies_df['genres'] = movies_df['genres'].apply(convert)
movies_df['keywords'] = movies_df['keywords'].apply(convert)
movies_df.head()

def convert3(obj):
    L = []
    counter = 0
    for i in ast.literal_eval(obj):
        if counter !=3:
            L.append(i['name'])
            counter +=1
        else:
            break
        return L
    
movies_df['cast'] = movies_df['cast'].apply(convert3)

movies_df.head()

def fetch_director(obj):
    L=[]
    for i in ast.literal_eval(obj):
        if i['job']=='Director':
            l.append(i['name'])
    return L

movies_df['crew']= movies_df['crew'].apply(fetch_director)

movies_df

movies_df['overview'][0]

movies_df['overview']= movies_df['overview'].apply(lambda x:x.split())

movies_df

movies_df['genres']= movies_df['genres'].apply(lambda x:[i.replace(" ","") for i in x])
movies_df['keywords']= movies_df['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
movies_df['cast']= movies_df['cast'].apply(lambda x:[i.replace(" ","") for i in x])
movies_df['crew']= movies_df['crew'].apply(lambda x:[i.replace(" ","") for i in x])

movies_df

movies_df['tags']= movies_df['overview']+movies_df['genres']+movies_df['keywords']+movies_df['cast']+movies_df['crew']

movies_df

new_df = movies_df[['movie_id','title','tags']]
new_df

new_df['tags']=new_df['tags'].apply(lambda x:' '.join(x))