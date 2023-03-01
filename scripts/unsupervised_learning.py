from unittest import result
import pandas as pd
import os
from variables import *
from functions import read_file
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt 
from sklearn.metrics import silhouette_score

unsupervised_df = pd.read_csv(learning_data)

unsupervised_df.drop(columns=["Unnamed: 0"],inplace=True)

print(unsupervised_df.isna().sum()) # There is no missing data

print(unsupervised_df.select_dtypes(include=["object"]).columns) #Category is the only categorial column
print(unsupervised_df.select_dtypes(exclude=["object"]).columns)

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

kmeans_file = os.path.join(FILE_PATH, "SSE.xlsx")
result = read_file(kmeans_file) 

result.set_index("K", inplace=True)  
print(result.plot())
plt.show()

kmeans=KMeans(n_clusters=10)
kmeans.fit(unsupervised_dummy)
unsupervised_dummy["Cluster"]=kmeans.labels_  

unsupervised_df.to_excel("unsupervised_df.xlsx")
unsupervised_dummy.to_excel("unsupervised_dummy.xlsx")

unsupervised_dummy.groupby("Cluster").describe().T.to_excel("results.xlsx") # Add to normalized data

unsupervised_df.groupby("Cluster").describe().T.to_excel("results2.xlsx") # Add to original data
