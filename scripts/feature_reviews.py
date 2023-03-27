import pandas as pd
from variables import *
from apps_exploration import apps
import matplotlib.pyplot as plt 
from Reviews_exploration import data as reviews
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import preprocessing


reviews.drop(columns=["Unnamed: 0"], inplace=True)

reviews_app_merge = pd.merge(apps, reviews, on= "App_Id")
reviews_app_merge.dropna(inplace=True)

le_geners = preprocessing.LabelEncoder()
reviews_app_merge["Geners"] = le_geners.fit_transform(reviews_app_merge["Geners"])
le_category = preprocessing.LabelEncoder()
reviews_app_merge["Category"] = le_category.fit_transform(reviews_app_merge["Category"])

x_train, x_test, y_train, y_test = train_test_split(reviews_app_merge.drop(columns=["App_name","Price"]), reviews_app_merge["Price"], test_size=0.3)

tree=RandomForestRegressor(n_estimators=100 , random_state=0)  
tree=tree.fit(x_train,y_train)
importances = tree.feature_importances_
print("Feature ranking:")
for feature, importance in zip(x_train.columns, importances):
    print("Feature:", feature, ",% Importance:", round(importance * 100, 2))

plt.figure(1, figsize=(8, 8))
plt.title("Feature importances")
plt.bar(range(x_train.shape[1]), importances, color="g", align="center")
plt.xticks(range(x_train.shape[1]), x_train.columns,rotation=90)
plt.xlim([-1, x_train.shape[1]])
plt.show() 

