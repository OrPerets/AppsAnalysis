import pandas as pd
import numpy as np
from variables import *
from functions import read_file


reviews = read_file(file_name_Reviews)

reviews.drop(columns=["No_reviews_count","Reviews_present_count","Unnamed: 0"], inplace=True)
print("There are", reviews.shape[0], "rows, and", reviews.shape[1], "columns.")
print("The columns in the Reviews table are:", reviews.columns)
print("The column types are:",reviews.dtypes)

print(reviews.isna().sum()) # There is no missing data

print("Information regarding the number of reviews:") 
# Not accurate, each has a recurring total number of reviews

print(reviews["Reviews_Number"].describe(percentiles=None))
print("Average review sentiment polarity:",reviews["Sentiment_Polarity"].mean()) 

# Checking the amount of good, medium, and bad reviews
# print("Number of good reviews:",data.loc[data['Sentiment_Polarity'] >= 0.3 , 'Sentiment_Polarity'].count())
# print("Number of medium reviews:",data.loc[(data['Sentiment_Polarity'] < 0.3) & (data['Sentiment_Polarity'] >= 0), 'Sentiment_Polarity'].count())
# print("Number of bad reviews:",data.loc[data['Sentiment_Polarity'] < 0 , 'Sentiment_Polarity'].count())
# print("Id of app with maximum reviews number:",data["Reviews_Number"].idxmax())
# print("Id of app with the best review rating:",data["Sentiment_Polarity"].idxmax())

# This is not accurate - prints the line number and not the actual app ID