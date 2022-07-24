import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn import linear_model
from sklearn import preprocessing
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import sklearn.metrics as metrics
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# plt.style.use("ggplot")

'''
OR: parameter name should be descriptive, instead of x use "file_name"
'''
def read_file(x):
    try:
        return pd.read_csv(x)
        print("Loaded")
    except:
        return "Eror"

'''
OR: x.value_counts() assumes that x is dataframe, should be called "df" or relative name
'''
def app_list(x):
    return pd.Series(x.value_counts().index)

#reading files
user_reviews=read_file("user_reviews.csv")
top_apps=read_file("top_apps.csv")
reviews=read_file("reviews.csv")
playstore2=read_file("playstore2.csv")
playstore1=read_file("playstore1.csv")
big_playstore=read_file("big_playstore.csv")      
apps=read_file("apps.csv")
android_games=read_file("android-games.csv")

#extracting apps columns 
user_reviews_apps=app_list(user_reviews["App"])
top_apps_colum=app_list(top_apps["App Name"])
reviews_apps=app_list(reviews["appId"])
playstore2_apps=app_list(playstore2["App"])
playstore1_apps=app_list(playstore1["App"])
big_playstore_apps=app_list(big_playstore["App Name"])
apps_from_apps_data=app_list(apps["title"])
android_games_apps=app_list(android_games["title"])

dictonary_app=pd.concat([user_reviews_apps,top_apps_colum,reviews_apps,playstore2_apps,playstore2_apps, 
playstore1_apps,big_playstore_apps,apps_from_apps_data,android_games_apps]).drop_duplicates(keep="first").reset_index(drop=True) #creating a series containing all apps names without duplicates

dictonary_app=dictonary_app.to_dict() 
dictonary_app = {value:key for (key,value) in dictonary_app.items()} #replacing the key and values order


