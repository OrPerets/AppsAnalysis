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

file_name = os.path.join(File_Path, "Rating.xlsx")
Rating = read_file(file_name)
print("Number of columns:",Rating.shape[1])
print("NUmber of Rows:",Rating.shape[0])
categorical_cols=Rating.select_dtypes(include=["object"]).columns
numerical_cols=Rating.select_dtypes(exclude=["object"]).columns
print("Categorical Columns:", categorical_cols)
print("Numerical Columns:",numerical_cols)
Rating.drop(columns=["Unnamed: 0"],inplace=True)
Rating=Rating.drop_duplicates(keep="first",ignore_index=True)
print(Rating.isna().sum())
