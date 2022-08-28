import pandas as pd
import numpy as np
import os
from variables import *
from functions import read_file

file_name = os.path.join(FILE_PATH, "App.xlsx")
apps = read_file(file_name)
categorical_cols=apps.select_dtypes(include=["object"]).columns
numerical_cols=apps.select_dtypes(exclude=["object"]).columns
apps.drop(columns=["Unnamed: 0"],inplace=True)  # Removing Unnamed column
apps=apps.drop_duplicates(keep="first",ignore_index=True ) # Removing rows with duplicate values


for col in categorical_cols:
    apps[col]=apps[col].apply(lambda x: str(x).lower()) # coverting all text to lowercases

condition=apps[(apps["App_Name_1"]==".") &(apps["App_Name_2"]==".") & (apps["App_Name_3"]==".") & (apps["App_Name_4"]==".")]
apps = apps.drop(condition.index)  #dropping rows that all 4 App_name column doesnt contains values


apps["App_name"]=apps[["App_Name_1","App_Name_2","App_Name_3","App_Name_4"]].apply(lambda x:
                            x.values[0] if x.values[0]==x.values[1] and x.values[2]=="." and x.values[3]=="." #column 0,1
                            else x.values[0] if x.values[0]==x.values[2] and x.values[1]=="." and x.values[3]=="." #column 0,2
                            else x.values[0] if x.values[0]==x.values[3] and x.values[1]=="." and x.values[2]=="." #column 0,3
                            else x.values[0] if x.values[0]==x.values[1] and x.values[0]==x.values[2] and x.values[3]=="." #column 0,1,2
                            else x.values[0] if x.values[0]==x.values[2] and x.values[0]==x.values[3] and x.values[1]=="." #columns 0,2,3
                            else x.values[1] if x.values[1]==x.values[2] and x.values[0]=="." and x.values[3]=="." #columns 1,2
                            else x.values[1] if x.values[1]==x.values[3] and x.values[0]=="." and x.values[0]=="." #columns 1,3
                            else x.values[1] if x.values[1]==x.values[2] and x.values[1]==x.values[3] and x.values[0]=="." #columns 1,2,3  
                            else x.values[2] if x.values[2]==x.values[3] and x.values[0]=="." and x.values[1]=="." #columns 2,3  
                            else x.values[0] if x.values[0]==x.values[1] and x.values[0] == x.values[2] and x.values[0] == x.values[3]  #columns 0,1,2,3  
                            else np.nan ,axis=1) 
print("Misiing values in App name column:",apps["App_name"].isna().sum())
apps.dropna(axis=0,inplace=True) #dropping Nan Values
apps.drop(columns=["App_Name_1","App_Name_2","App_Name_3","App_Name_4"],inplace=True) #Dropping the initial app name columns
apps=apps.reindex(columns=["App_Id","App_name","Price","Geners","Category"]) #orginazing columns order
apps=apps.reset_index(drop=True)
print(apps)
apps.to_excel("Apps_3.0.xlsx")
