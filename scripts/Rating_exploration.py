import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from variables import *
from functions import read_file

file_name = os.path.join(FILE_PATH, "Rating.xlsx")
rating = read_file(file_name)
print("Number of columns:",rating.shape[1])
print("NUmber of Rows:",rating.shape[0])
categorical_cols=rating.select_dtypes(include=["object"]).columns
numerical_cols=rating.select_dtypes(exclude=["object"]).columns
print("Categorical Columns:", categorical_cols)
print("Numerical Columns:",numerical_cols)
rating.drop(columns=["Unnamed: 0"],inplace=True)
Rating=rating.drop_duplicates(keep="first",ignore_index=True)
print(Rating.isna().sum())
