from variables import *
from functions import read_file

installs=read_file(file_name_Installs)

installs.drop(columns=["Unnamed: 0"],inplace=True)  
print("There are",installs.shape[0],"Rows and", installs.shape[1],"Columns")

categorical_cols=installs.select_dtypes(include=["object"]).columns
numerical_cols=installs.select_dtypes(exclude=["object"]).columns
print("categorical_columns:", categorical_cols)
print("numerical_columns:",numerical_cols)
installs=installs.drop_duplicates(keep="first",ignore_index=True ) 

