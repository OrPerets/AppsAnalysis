import pandas as pd
import os
import requests
from datetime import date

SERVER_URL = "https://app-server-three.vercel.app"

def read_file(file_name):
    try:
        if os.environ["IS_PROD"]:
            return fetch_data(file_name.split(".")[0])
    except:
        try:
            return pd.read_excel(file_name)
        except:
            return "Error"

# in case of remote DB - retrieve the first 100 records of a given collection
def fetch_data(collection, size=100):
    try:
        data = requests.get(SERVER_URL + "/getItems/" + collection + "/" + str(size))
        return pd.DataFrame(data.json())
    except Exception as e:
        return "Error"

fetch_data("Rating")
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


def get_year(yearDate):
    today = date.today()
    return today.year - yearDate

#Remove empty space
def remove_space(w):
    if type(w) != str:
        return w
    return w.strip()

