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

#String to Int convertor
def str_to_int(s):
    if type(s) == int:
        return s
    elif s.isnumeric() == True:
        return int(s)
    n = ''
    for i in s:
        if i.isnumeric() == True:
            n += i
    return int(n)

#Age to date convertor
from datetime import date
def get_year(yearDate):
    today = date.today()
    return today.year - yearDate

#Remove empty space
def remove_space(w):
    if type(w) != str:
        return w
    return w.strip()

# data_name_list = [os.path.join(FILES_PATH,f) for f in listdir(FILES_PATH) if isfile(join(FILES_PATH, f))]

# df_dict is a dictrionary mapping file name to file dataframe
# df_dict = read_all_datas(data_name_list)





