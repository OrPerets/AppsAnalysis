import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from variables import *
from functions import read_file

rating=read_file(file_name_Rating)

rating["Rating"]=rating["Rating"].apply(lambda x: 1 if x<=1 else
                                                  2 if x>1 and x <=2 else
                                                  3 if x>2 and x <=3 else
                                                  4 if x>3 and x<=4 else 5)  #Turning test group to categorical   

x_train, x_test, y_train, y_test = train_test_split(rating.drop(columns=["Unnamed: 0","App_Id","Rating"]), rating["Rating"], test_size=0.3)
tree=RandomForestClassifier(n_estimators=100)
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
print(zip(x_train.columns, importances))