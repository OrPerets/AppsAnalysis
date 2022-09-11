from traceback import print_tb
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from variables import *
from functions import read_file
from sklearn.ensemble import RandomForestRegressor
from sklearn import preprocessing

# Reading & Exploring files    
from apps_exploration import *
print(apps.head())    

from reviews_exploration import *
print(reviews.head())

from installs_exploration import *
print(installs.head())

from rating_exploration import *
print(rating.head())

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
