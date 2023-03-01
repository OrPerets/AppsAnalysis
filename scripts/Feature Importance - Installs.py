import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from variables import *
from functions import read_file
from sklearn.ensemble import RandomForestRegressor
from sklearn import preprocessing
from sklearn import metrics

apps=read_file(file_name_Apps)
installs=read_file(file_name_Installs)

merged_df=pd.merge(apps,installs,on="App_Id")
merged_df.drop(columns=["Unnamed: 0_x","Unnamed: 0_y"],inplace=True)

le_geners = preprocessing.LabelEncoder()
merged_df["Geners"] = le_geners.fit_transform(merged_df["Geners"])
le_category = preprocessing.LabelEncoder()
merged_df["Category"] = le_category.fit_transform(merged_df["Category"])

x_train, x_test, y_train, y_test = train_test_split(merged_df.drop(columns=["App_Id","App_name","Installs"]), merged_df["Installs"], test_size=0.3)

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

