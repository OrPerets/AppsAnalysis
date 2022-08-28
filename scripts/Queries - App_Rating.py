import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from variables import *
from functions import read_file

rating = read_file(file_name_Rating)
apps=read_file(file_name_Apps)
apps.drop(columns=["Unnamed: 0"],inplace=True)
rating.drop(columns=["Unnamed: 0","Thumbs_Up_Count"],inplace=True)
merged_df=pd.merge(apps,rating,on="App_Id")
merged_df.dropna(inplace=True)
merged_df=merged_df.drop(merged_df[merged_df["Geners"]=="."].index)

#Queries:
print("1. Category with the highest rating average is",merged_df.groupby("Category")["Rating"].mean().idxmax())
print("2. The expensivest app:",merged_df[merged_df["Price"]==merged_df["Price"].max()]["App_name"],
     "and it cost",merged_df["Price"].max(),"$")

merged_df_price_Rating=merged_df[["Price","Rating"]].copy()
merged_df_price_Rating["Price"]=merged_df_price_Rating["Price"].apply(lambda x: "paid" if x>0 else "free")
print("3.",merged_df_price_Rating.groupby("Price")["Rating"].mean().idxmax(), "Apps", "has higher rating average then", 
merged_df_price_Rating.groupby("Price")["Rating"].mean().idxmin())

print("4. The least frequent category is:",merged_df["Category"].value_counts().index[-1])
print("5. The most frequent category is:",merged_df["Category"].value_counts().index[0])
print("6. Family category rating average:",merged_df[merged_df["Category"]=="family"]["Rating"].mean())
print("7. The App that got the highest 5 star rating is",         
list(merged_df[merged_df["5 Star ratings"]==merged_df["5 Star ratings"].max()]["App_name"])[0])
print("8. Conclusion from the graph: Paid apps have a high rating score, no less then 3.0")
print("9. Conclusion from the graph: Of all apps that have the highest Rating score (5.0), apps that belongs to family category, appears the most.")
print("10. Conclusion from the graph: Of al apps that have the lowest Rating score (1.0), apps that belongs to medical,family and tools geners, appears the most.")

merged_df.plot.scatter(x='Rating', y="Price", title="Rating & Price")
plt.show()     
merged_df[merged_df["Rating"]==merged_df["Rating"].max()]["Category"].value_counts().plot(kind="bar",title="Categories Popularity For Apps With Maximum Rating")
plt.show()     
merged_df[merged_df["Rating"]==merged_df["Rating"].min()]["Category"].value_counts().plot(kind="pie",autopct="%1.2f%%",title="Categories Popularity For Apps With Minimun Rating")
plt.show()     

