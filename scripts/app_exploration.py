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

file_name = os.path.join(File_Path, "App.xlsx")
App = read_file(file_name)
print("Number of Rows:", App.shape[0])
print("Number of Columns:", App.shape[1])
print(App.columns)
categorical_cols=App.select_dtypes(include=["object"]).columns
numerical_cols=App.select_dtypes(exclude=["object"]).columns
print("Categorical Columns:", categorical_cols)
print("Numerical Columns:",numerical_cols)
App.drop(columns=["Unnamed: 0"],inplace=True)  # Removing Unnamed column
print(App.isna().sum())
App=App.drop_duplicates(keep="first",ignore_index=True ) # Removing rows with duplicate values



