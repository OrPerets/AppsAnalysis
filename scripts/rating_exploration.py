from logging.handlers import RotatingFileHandler
import pandas as pd
from variables import *
from functions import read_file

rating=read_file(file_name_Rating)
rating.drop(columns=["Unnamed: 0"],inplace=True)
print("There are",rating.shape[0],"Rows and", rating.shape[1],"Columns")
categorical_cols=rating.select_dtypes(include=["object"]).columns
numerical_cols=rating.select_dtypes(exclude=["object"]).columns
print("categorical_columns:", categorical_cols)
print("numerical_columns:",numerical_cols)
print(rating.isna().sum())
rating=rating.drop_duplicates(keep="first",ignore_index=True ) # Removing rows with duplicate values



