import pandas as pd
from variables import *
import functools as ft

# Reading & Exploring files    
from apps_exploration import *
print(apps.head()) 
apps_top_features = ['App_Id', 'Price', 'Category'] 

from reviews_exploration import *
print(reviews.head())
reviews_top_features = ['App_Id', 'Sentiment','Reviews_Number']

from installs_exploration import *
print(installs.head())
installs_top_features = ['App_Id', 'Growth (60 days)', 'Installs']

from rating_exploration import *
print(rating.head())
rating_top_features = ['App_Id', '1 Star ratings', '5 Star ratings', 'Thumbs_Up_Count', 'Rating']

# Queries 
print()
print("Queries for Apps & Rating charts")
from queries_app_rating import *
print()
print("Queries for Apps & Reviews charts")
from reviews_queries import *
print()
print("Queries for Apps & Installs charts")
from queries_app_installs import *


dfs = [
       apps[apps_top_features], 
       reviews[reviews_top_features], 
       installs[installs_top_features],
       rating[rating_top_features]
       ]

data = ft.reduce(lambda left, right: pd.merge(left, right, on='App_Id'), dfs)
data.to_csv("learning_data.csv")
