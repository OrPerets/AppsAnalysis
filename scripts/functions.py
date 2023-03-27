import pandas as pd
import os
from functools import reduce
import numpy as np
import json
import requests
from datetime import date


def read_file(file_name):
    try:
        return pd.read_excel(file_name)
    except:
        return "Error"

def read_all_datas(data_name_list):   
    files = {}
    for data_name in data_name_list:
        files[data_name] = read_file(data_name)
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
def get_year(yearDate):
    today = date.today()
    return today.year - yearDate

def fetchData(name):
    response = requests.get('https://appsanalysis.vercel.app/getItems/'+name)
    return response.json()

#Remove empty space
def remove_space(w):
    if type(w) != str:
        return w
    return w.strip()

