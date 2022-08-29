import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from variables import *
from functions import read_file
from sklearn.ensemble import RandomForestRegressor

installs= read_file(file_name_Installs)

x_train, x_test, y_train, y_test = train_test_split(installs.drop(columns=["Unnamed: 0","App_Id","Installs"]), installs["Installs"], test_size=0.3)

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

