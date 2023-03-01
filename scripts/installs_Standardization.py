import os
from variables import *
from functions import read_file

file_name = os.path.join(FILE_PATH, "Installs.xlsx")
installs = read_file(file_name)

categorical_cols=installs.select_dtypes(include=["object"]).columns
numerical_cols=installs.select_dtypes(exclude=["object"]).columns
installs.drop(columns=["Unnamed: 0"],inplace=True) 
print(installs.isna().sum())
installs=installs.drop_duplicates(keep="first",ignore_index=True ) 
installs.to_excel("Installs_3.0.xlsx")
