import re
import pandas as pd
import numpy as np
import os
from variables import *
from functions import read_file
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt 
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing
from sklearn import metrics


unsupervised_df = pd.read_csv(learning_data)

unsupervised_df.drop(columns=["Unnamed: 0"],inplace=True)

# print(unsupervised_df.isna().sum()) # There is no missing data

# print(unsupervised_df.select_dtypes(include=["object"]).columns) #Category is the only categorial column
# print(unsupervised_df.select_dtypes(exclude=["object"]).columns)

unsupervised_df.drop(unsupervised_df[unsupervised_df['Category'] =='.'].index, inplace=True)
unsupervised_dummy=pd.get_dummies(unsupervised_df)

for col in ["App_Id","Price","Sentiment","Reviews_Number","Growth (60 days)","Installs","1 Star ratings","5 Star ratings","Thumbs_Up_Count"]:
    unsupervised_dummy[col] = (unsupervised_dummy[col] - unsupervised_dummy[col].mean()) / unsupervised_dummy[col].std()

def get_kmeans_accuracy(data, top_k):
    sum_squared = []
    silhouette = []
    K = range(2, top_k)
    for i in K:
        kmeans = KMeans(n_clusters = i, init = 'k-means++')
        kmeans.fit(data)
        sum_squared.append(kmeans.inertia_)         
        silhouette.append(silhouette_score(data, kmeans.labels_))    
    return pd.DataFrame({
    "K": K,
    "SSE": sum_squared,
    "SIL": silhouette
  })
result=get_kmeans_accuracy(unsupervised_dummy,20)  
result.set_index("K", inplace=True)  
# print(result.plot(subplots=True))
print("STARTED")
# print(result)

print("FINISHED")