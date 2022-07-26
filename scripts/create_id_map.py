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
plt.style.use("ggplot")


def read_file(file_name):
    try:
        return pd.read_csv(file_name)
        
    except:
        return "Eror"
def app_list(df):
    return pd.Series(df.value_counts().index)

#reading files
user_reviews=read_file("user_reviews.csv")
top_apps=read_file("top_apps.csv")
reviews=read_file("reviews.csv")
playstore2=read_file("playstore2.csv")
playstore1=read_file("playstore1.csv")
big_playstore=read_file("big_playstore.csv")      
apps=read_file("apps.csv")
android_games=read_file("android-games.csv")

#creating a series containing all apps names without duplicates
dictonary_app=pd.concat([user_reviews["App"],top_apps["App Name"],reviews["appId"],playstore2["App"],playstore1["App"], 
big_playstore["App Name"],apps["title"],android_games["title"]]).drop_duplicates(keep="first").reset_index(drop=True) 

dictonary_app=dictonary_app.to_dict() #turning the pandas Series to a dictonary
dictonary_app = {value:key for (key,value) in dictonary_app.items()} #replacing the key and values order

#adding a new app ID column for each DataFrame 
def App_Id_Seal(df,df_app_column):
    df["app_id_new"]=df_app_column.astype(str).map(dictonary_app)

App_Id_Seal(user_reviews,user_reviews["App"])
App_Id_Seal(top_apps,top_apps["App Name"])
App_Id_Seal(reviews,reviews["appId"])
App_Id_Seal(playstore1,playstore1["App"])
App_Id_Seal(playstore2,playstore2["App"])
App_Id_Seal(big_playstore,big_playstore["App Name"])
App_Id_Seal(apps,apps["title"])
App_Id_Seal(android_games,android_games["title"])

