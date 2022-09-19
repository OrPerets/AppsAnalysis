from tkinter import scrolledtext
from variables import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
import math
from sklearn import metrics
from sklearn.metrics import accuracy_score, confusion_matrix, mean_squared_error
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm

# Reading data
try:
    data=pd.read_csv(file_name_learning_data)
except:
    print("Error")

data.drop(columns=["Unnamed: 0","App_Id"],inplace=True)

print(data.isna().sum()) #--> No missing values    

le = preprocessing.LabelEncoder()
data["Category"]=le.fit_transform(data["Category"])
normalized_data=data.copy()
scalar=MinMaxScaler()
scalar.fit_transform(normalized_data)
normalized_data=pd.DataFrame(scalar.fit_transform(normalized_data) ,columns=normalized_data.columns)
X=normalized_data.drop(columns=["Price"]).copy()
Y=normalized_data["Price"].copy()
print(X)
## Price colunm as test group--> Using RandomForestRegressor Algorithem

# X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=42)
# Regressor_tree=RandomForestRegressor(n_estimators=100 , random_state=42)  
# Regressor_tree.fit(X_train,y_train)
# Regressor_tree_prediction = Regressor_tree.predict(X_test) # Make predictions for the test set
# mse = mean_squared_error(y_test, Regressor_tree_prediction)
# rmse = mse**0.5
# print("Mean squared error for RandomForestRegressor:",mse)
# print("Root of Mean squared error for RandomForestRegressor: ",rmse)
# print("RandomForestRegressor score",r2_score(y_test,Regressor_tree_prediction))

# ## Price colunm as test group--> Using LinearRegression Algorithem
# linear_tree=LinearRegression()
# linear_tree.fit(X_train, y_train)
# linear_prediction = linear_tree.predict(X_test)
# print('Mean Squared Error for LinearRegression:', metrics.mean_squared_error(y_test, linear_prediction))
# print('Root Mean Squared Error for LinearRegression:', np.sqrt(metrics.mean_squared_error(y_test, linear_prediction)))
# print("LinearRegression score:",r2_score(y_test,linear_prediction))

# # For Price colunm as test group, it's impossible to do confusion matrix because test group is continuous

# ## Rating column as test group --> Using RandomForestClassifier

# df_for_rating=data.copy()
# df_for_rating["Rating"]=df_for_rating["Rating"].apply(lambda x: math.floor(x) if x + 0.5 == math.ceil(x) else round(x)) # Roung rating column
# X=df_for_rating.drop(columns=["Rating"]).copy()
# Y=df_for_rating["Rating"].copy()
# X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=42)
# forest=RandomForestClassifier(n_estimators=100, random_state=42) # practicing on 100 diffrent trees
# forest.fit(X_train, y_train)
# y_pred = forest.predict(X_test)
# print("Accuracy score for RandomForestClassifier:",metrics.accuracy_score(y_test, y_pred))
# print("Cunfusion Matrix for RandomForestClassifier:\n",confusion_matrix(y_test,y_pred))

# ## Rating column as test group --> Using KNeighborsClassifier

# knn_df=pd.DataFrame(scalar.fit_transform(X),columns=X.columns) #normalizing the DataFrame without rating column
# knn_df["Rating"]=Y
# X_train, X_test, y_train, y_test = train_test_split(knn_df.drop(columns=["Rating"]), knn_df["Rating"], test_size=0.25, random_state=42)

# Knn_Classifier=KNeighborsClassifier(n_neighbors=3)
# Knn_Classifier.fit(X_train,y_train)
# KNN_pred=Knn_Classifier.predict(X_test)
# print("KNN accuracy score:",metrics.accuracy_score(KNN_pred,y_test))
# print("Cunfusion Matrix for KNeighborsClassifier:\n",confusion_matrix(y_test,KNN_pred))

# # Rating column as test group--> Using SVM 
# svm_classifier=svm.SVC(kernel="linear")
# svm_classifier.fit(X_train,y_train)
# y_pred=svm_classifier.predict(X_test)
# print("SVM accuracy score:",metrics.accuracy_score(y_test, y_pred))


