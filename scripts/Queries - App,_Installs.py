#from gettext import install
import numpy as np
import pandas as pd
import os
from variables import *
from functions import read_file
import matplotlib.pyplot as plt

installs = read_file(file_name_Installs)
apps=read_file(file_name_Apps)

apps.drop(columns=["Unnamed: 0"],inplace=True)
installs.drop(columns=["Unnamed: 0"],inplace=True)
merged_df=pd.merge(apps,installs,on="App_Id")
merged_df.isna().sum()
merged_df.dropna(inplace=True)

#Queries:
print("1. Installs Average:",merged_df["Installs"].mean())
print("2.",float(merged_df["Price"].value_counts(normalize=True).head(1)*100),"%", "of all apps, are free")
print("3. Number of apps with the most installs is:",merged_df[merged_df["Installs"]==merged_df["Installs"].max()].shape[0])
print("4. Top" ,merged_df[merged_df["Installs"]==merged_df["Installs"].max()].shape[0] ,"Apps:",list(merged_df[merged_df["Installs"]==merged_df["Installs"].max()]["App_name"]))
print("5. Highest number of Installs:",float(merged_df[merged_df["Installs"]==merged_df["Installs"].max()]["Installs"].head(1)))
print("6. Number on installs for the expensivest apps is:",float(merged_df[merged_df["Price"]==merged_df["Price"].max()]["Installs"]))
print("7. Conclusion from the graph: Apps with most Installs belongs to communication genre") 
print("8. Conclusion from the graph: There had been more installs for apps that has price range between 0-50 $, rather then apps that costs more then 50$.")
print("9. Conclusion from the graph: Finance, Education and Social apps geners has the lowest installs rate.")
print("10. Conclusion from the graph: Free apps has higher rate growth in 30 days compared to paid apps.")

merged_df[merged_df["Installs"]==merged_df["Installs"].max()]["Geners"].value_counts().plot(kind="bar",title ="Geners Popularity With Highest Installs")
plt.show()
merged_df.plot.scatter(x="Price",y="Installs", title="Price & Installs")
plt.show()
merged_df[merged_df["Installs"]==merged_df["Installs"].min()]["Geners"].value_counts().plot(kind="pie",autopct="%1.2f%%",title="Geners Popularity With Minimum Installs")
plt.show()
merged_df.plot.scatter(x="Price" ,y= "Growth (30 days)",title="Growth in 30 days according to apps prices")
plt.show()
