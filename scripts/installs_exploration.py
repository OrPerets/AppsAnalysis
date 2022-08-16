import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
File_Path=os.path.join(os.getcwd(), "data-warehouse")

def read_file(file_name):
    try:
        return pd.read_excel(file_name)
        
    except:
        return "Error"

file_name = os.path.join(File_Path, "Installs.xlsx")
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


