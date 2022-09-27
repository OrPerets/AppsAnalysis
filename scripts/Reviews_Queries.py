import re
import pandas as pd
import os
from variables import *
from functions import read_file
from reviews_exploration import data
from apps_exploration import apps
import matplotlib.pyplot as plt 
import numpy as np

apps=read_file(file_name_Apps)
reviews = read_file(file_name_Reviews)

apps.drop(columns=["Unnamed: 0"],inplace=True)
reviews.drop(columns=["Unnamed: 0"],inplace=True)
merged_df=pd.merge(apps,reviews,on="App_Id")
print(merged_df["Sentiment_Polarity"].describe())
print(merged_df["Sentiment"].describe())

# # As seen by the .describe - there are no outliers in the Reviews table

merged_df.dropna(inplace=True)

# QUERIES :
reviews_app_merge = pd.merge(apps, data, on= "App_Id")
reviews_app_merge.dropna(inplace=True)

condition=reviews_app_merge[(reviews_app_merge["App_Name_1"]==".") &(reviews_app_merge["App_Name_2"]==".") & (reviews_app_merge["App_Name_3"]==".") & (reviews_app_merge["App_Name_4"]==".")]
reviews_app_merge = reviews_app_merge.drop(condition.index)  #dropping rows that all 4 App_name column doesnt contains values


reviews_app_merge["App_name"]=reviews_app_merge[["App_Name_1","App_Name_2","App_Name_3","App_Name_4"]].apply(lambda x:
                            x.values[0] if x.values[0]==x.values[1] and x.values[2]=="." and x.values[3]=="." #column 0,1
                            else x.values[0] if x.values[0]==x.values[2] and x.values[1]=="." and x.values[3]=="." #column 0,2
                            else x.values[0] if x.values[0]==x.values[3] and x.values[1]=="." and x.values[2]=="." #column 0,3
                            else x.values[0] if x.values[0]==x.values[1] and x.values[0]==x.values[2] and x.values[3]=="." #column 0,1,2
                            else x.values[0] if x.values[0]==x.values[2] and x.values[0]==x.values[3] and x.values[1]=="." #columns 0,2,3
                            else x.values[1] if x.values[1]==x.values[2] and x.values[0]=="." and x.values[3]=="." #columns 1,2
                            else x.values[1] if x.values[1]==x.values[3] and x.values[0]=="." and x.values[0]=="." #columns 1,3
                            else x.values[1] if x.values[1]==x.values[2] and x.values[1]==x.values[3] and x.values[0]=="." #columns 1,2,3  
                            else x.values[2] if x.values[2]==x.values[3] and x.values[0]=="." and x.values[1]=="." #columns 2,3  
                            else x.values[0] if x.values[0]==x.values[1] and x.values[0] == x.values[2] and x.values[0] == x.values[3]  #columns 0,1,2,3  
                            else np.nan ,axis=1)

reviews_app_merge.drop(columns=["App_Name_1","App_Name_2","App_Name_3","App_Name_4"],inplace=True) #Dropping the initial app name columns

print(reviews_app_merge.head())

# Checking the amount of good, mediocre, and bad reviews to see what's most common
print("Number of good reviews:",merged_df.loc[merged_df['Sentiment_Polarity'] >= 0.3 , 'Sentiment_Polarity'].count())
print("Number of mediocre reviews:",merged_df.loc[(merged_df['Sentiment_Polarity'] < 0.3) & (merged_df['Sentiment_Polarity'] >= 0), 'Sentiment_Polarity'].count())
print("Number of bad reviews:",merged_df.loc[merged_df['Sentiment_Polarity'] < 0 , 'Sentiment_Polarity'].count())

print("Name of app with maximum reviews number:" , merged_df[['App_name']][merged_df.Reviews_Number == merged_df.Reviews_Number.max()])
print("Name of app with minimum reviews number:" , merged_df[['App_name']][merged_df.Reviews_Number == merged_df.Reviews_Number.min()])

app_groups=merged_df.groupby("App_name")["Sentiment"].mean()
print("Apps by their review rating average:",app_groups.sort_values(ascending=False))

# '''
mean_sentiment = merged_df.groupby("App_name")["Sentiment"].mean()
max_sentiment = mean_sentiment.max()
print("Name of app with best review rating:" , mean_sentiment[mean_sentiment == max_sentiment])
# '''

# # New column = positive/negative based on the sentiment column:
merged_df["Verbal Sentiment"]=merged_df["Sentiment"].apply(lambda x: 'Positive' if x>0 else 'Negative')

print("Positive reviews vs negative reviews:")
print(merged_df["Verbal Sentiment"].value_counts())
print()
print("Top 3 most common genre:",merged_df["Geners"].value_counts().head(3))
print("Top 3 most common category:", merged_df["Category"].value_counts().head(3))

print("Conclusions:")
print()
print("1. Sports is a very common theme for an app")
print("2. Facebook has the most reviews - as expected big apps have more reviews")
print("3. On average, people tend to rate apps in the middle between bad and good, and they usually don't rate badly")
print("4. There are almost 6 times positive reviews vs negative reviews")
print("5. Apps with positive sentiment have a higher price")
print(merged_df.groupby("Verbal Sentiment")["Price"].mean().plot(kind="bar",legend=True, title="Price effect on sentiment")) # See how the price affects the reviews

## Graphs for future plotting
#plt.show()

# # See which Genres tend to be more expensive:
print(merged_df.groupby("Geners")["Price"].mean().plot(kind="barh"))
#plt.show()