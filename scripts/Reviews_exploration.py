from variables import *
from functions import read_file

reviews = read_file(file_name_Reviews)

reviews.drop(columns=["No_reviews_count","Reviews_present_count","Unnamed: 0"], inplace=True)
print("There are", reviews.shape[0], "rows, and", reviews.shape[1], "columns.")
print("The columns in the Reviews table are:", reviews.columns)
print("The column types are:",reviews.dtypes)

print("Information regarding the number of reviews:") 

print(reviews["Reviews_Number"].describe(percentiles=None))
print("Average review sentiment polarity:",reviews["Sentiment_Polarity"].mean()) 
