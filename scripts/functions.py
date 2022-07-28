#import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import silhouette_score
#import seaborn as sns
from os import listdir
import os
from os.path import isfile, join

FILES_PATH = os.path.join(os.getcwd(), "data-sources")
# print(FILES_PATH)

def read_csv_file(data_name):  # reads data from a file (returns the file as a dataframe)
    try:
        df=pd.read_csv(data_name)
        print("File Loaded")
        return df
    except:
        return "Error"

# reads the data from all of the files and adds the data into a dictionary
# key is the file's name, value is the dataframe

def read_all_datas(data_name_list):   
    files = {}
    for data_name in data_name_list:
        files[data_name] = read_csv_file(data_name)
    return files

data_name_list = [os.path.join(FILES_PATH,f) for f in listdir(FILES_PATH) if isfile(join(FILES_PATH, f))]

# df_dict is a dictrionary mapping file name to file dataframe
df_dict = read_all_datas(data_name_list)





