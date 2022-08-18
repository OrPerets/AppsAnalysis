import pandas as pd
import os
from variables import *
from functions import read_file

file_name = os.path.join(FILE_PATH, "Installs.xlsx")
installs = read_file(file_name)
print("Number of Rows:", installs.shape[0])
print("Number of Columns:", installs.shape[1])
print(installs.columns)
categorical_cols=installs.select_dtypes(include=["object"]).columns
numerical_cols=installs.select_dtypes(exclude=["object"]).columns
print("Categorical Columns:", categorical_cols)
print("Numerical Columns:",numerical_cols)
installs.drop(columns=["Unnamed: 0"],inplace=True)  # Removing Unnamed column
print(installs.isna().sum())
installs=installs.drop_duplicates(keep="first",ignore_index=True ) # Removing rows with duplicate values


