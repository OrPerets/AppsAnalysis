import pandas as pd
import os
from variables import *
from functions import read_file

#file_name = os.path.join(FILE_PATH, "App.xlsx")
apps = read_file(file_name_Apps)
apps.drop(columns=["Unnamed: 0"],inplace=True)  # Removing Unnamed column

print("Number of Rows:", apps.shape[0])
print("Number of Columns:", apps.shape[1])
print(apps.columns)
categorical_cols=apps.select_dtypes(include=["object"]).columns
numerical_cols=apps.select_dtypes(exclude=["object"]).columns
print("Categorical Columns:", categorical_cols)
print("Numerical Columns:",numerical_cols)
print(apps.isna().sum())
apps.dropna(inplace=True) #removing missing values
apps=apps.drop_duplicates(keep="first",ignore_index=True ) # Removing rows with duplicate values

