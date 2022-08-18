import pandas as pd
import os
from variables import *
from functions import read_file

file_name = os.path.join(FILE_PATH, "Rating.xlsx")
REVIEWS =  os.path.join(FILE_PATH, "Reviews.xlsx")

data = read_file(REVIEWS)

data.drop(columns=["No_reviews_count","Reviews_present_count"], inplace=True)

print("There are", data.shape[0], "rows, and", data.shape[1], "columns.")
print("The columns in the Reviews table are:", data.columns)
print("The column types are:",data.dtypes)

print(data.isna().sum()) # There is no missing data

print("Information regarding the number of reviews:") 
# Not accurate, each has a recurring total number of reviews

print(data["Reviews_Number"].describe(percentiles=None))
print("Average review sentiment polarity:",data["Sentiment_Polarity"].mean()) 

# Checking the amount of good, medium, and bad reviews
# print("Number of good reviews:",data.loc[data['Sentiment_Polarity'] >= 0.3 , 'Sentiment_Polarity'].count())
# print("Number of medium reviews:",data.loc[(data['Sentiment_Polarity'] < 0.3) & (data['Sentiment_Polarity'] >= 0), 'Sentiment_Polarity'].count())
# print("Number of bad reviews:",data.loc[data['Sentiment_Polarity'] < 0 , 'Sentiment_Polarity'].count())
# print("Id of app with maximum reviews number:",data["Reviews_Number"].idxmax())
# print("Id of app with the best review rating:",data["Sentiment_Polarity"].idxmax())

# This is not accurate - prints the line number and not the actual app ID
