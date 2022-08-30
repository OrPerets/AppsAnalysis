import re
import pandas as pd
import os
from variables import *
from functions import read_file
from Reviews_exploration import data
#from app_exploration import apps
import matplotlib.pyplot as plt 
import numpy as np

print("*******************************")


read_file(file_name_Reviews)

print(read_file)
# data.drop(columns=["Unnamed: 0"], inplace=True)

# print(data["Sentiment_Polarity"].describe())
# print(data["Sentiment"].describe())

# # As seen by the .describe - there are no outliers in the Reviews table

# reviews_app_merge = pd.merge(apps, data, on= "App_Id")
# reviews_app_merge.dropna(inplace=True)

# condition=reviews_app_merge[(reviews_app_merge["App_Name_1"]==".") &(reviews_app_merge["App_Name_2"]==".") & (reviews_app_merge["App_Name_3"]==".") & (reviews_app_merge["App_Name_4"]==".")]
# reviews_app_merge = reviews_app_merge.drop(condition.index)  #dropping rows that all 4 App_name column doesnt contains values


# reviews_app_merge["App_name"]=reviews_app_merge[["App_Name_1","App_Name_2","App_Name_3","App_Name_4"]].apply(lambda x:
#                             x.values[0] if x.values[0]==x.values[1] and x.values[2]=="." and x.values[3]=="." #column 0,1
#                             else x.values[0] if x.values[0]==x.values[2] and x.values[1]=="." and x.values[3]=="." #column 0,2
#                             else x.values[0] if x.values[0]==x.values[3] and x.values[1]=="." and x.values[2]=="." #column 0,3
#                             else x.values[0] if x.values[0]==x.values[1] and x.values[0]==x.values[2] and x.values[3]=="." #column 0,1,2
#                             else x.values[0] if x.values[0]==x.values[2] and x.values[0]==x.values[3] and x.values[1]=="." #columns 0,2,3
#                             else x.values[1] if x.values[1]==x.values[2] and x.values[0]=="." and x.values[3]=="." #columns 1,2
#                             else x.values[1] if x.values[1]==x.values[3] and x.values[0]=="." and x.values[0]=="." #columns 1,3
#                             else x.values[1] if x.values[1]==x.values[2] and x.values[1]==x.values[3] and x.values[0]=="." #columns 1,2,3  
#                             else x.values[2] if x.values[2]==x.values[3] and x.values[0]=="." and x.values[1]=="." #columns 2,3  
#                             else x.values[0] if x.values[0]==x.values[1] and x.values[0] == x.values[2] and x.values[0] == x.values[3]  #columns 0,1,2,3  
#                             else np.nan ,axis=1)

# reviews_app_merge.drop(columns=["App_Name_1","App_Name_2","App_Name_3","App_Name_4"],inplace=True) #Dropping the initial app name columns

# # QUERIES :

# # Checking the amount of good, mediocre, and bad reviews to see what's most common
# print("Number of good reviews:",reviews_app_merge.loc[reviews_app_merge['Sentiment_Polarity'] >= 0.3 , 'Sentiment_Polarity'].count())
# print("Number of mediocre reviews:",reviews_app_merge.loc[(reviews_app_merge['Sentiment_Polarity'] < 0.3) & (reviews_app_merge['Sentiment_Polarity'] >= 0), 'Sentiment_Polarity'].count())
# print("Number of bad reviews:",reviews_app_merge.loc[reviews_app_merge['Sentiment_Polarity'] < 0 , 'Sentiment_Polarity'].count())

# print("Name of app with maximum reviews number:" , reviews_app_merge[['App_name']][reviews_app_merge.Reviews_Number == reviews_app_merge.Reviews_Number.max()])
# print("Name of app with minimum reviews number:" , reviews_app_merge[['App_name']][reviews_app_merge.Reviews_Number == reviews_app_merge.Reviews_Number.min()])

# app_groups=reviews_app_merge.groupby("App_name")["Sentiment"].mean()
# print("Apps by their review rating average:",app_groups.sort_values(ascending=False))

# '''
# mean_sentiment = reviews_app_merge.groupby("App_name")["Sentiment"].mean()
# max_sentiment = mean_sentiment.max()
# print("Name of app with best review rating:" , mean_sentiment[mean_sentiment == max_sentiment])

# '''

# # New column = positive/negative based on the sentiment column:
# reviews_app_merge["Verbal Sentiment"]=reviews_app_merge["Sentiment"].apply(lambda x: 'Positive' if x>0 else 'Negative')

# print(reviews_app_merge.groupby("Verbal Sentiment")["Price"].mean().plot(kind="bar",legend=True, title="Price effect on sentiment")) # See how the price affects the reviews
# plt.show()

# # See which Genres tend to be more expensive:
# print(reviews_app_merge.groupby("Geners")["Price"].mean().plot(kind="barh"))
# plt.show()

# print("Positive reviews vs negative reviews:")
# print(reviews_app_merge["Verbal Sentiment"].value_counts())
# print()
# print("Top 3 most common genre:",reviews_app_merge["Geners"].value_counts().head(3))
# print("Top 3 most common category:", reviews_app_merge["Category"].value_counts().head(3))

# print("Conclusions:")
# print()
# print("1. Sports is a very common theme for an app")
# print("2. Facebook has the most reviews - as expected big apps have more reviews")
# print("3. On average, people tend to rate apps in the middle between bad and good, and they usually don't rate badly")
# print("4. There are almost 6 times positive reviews vs negative reviews")
# print("5. Apps with positive sentiment have a higher price")

