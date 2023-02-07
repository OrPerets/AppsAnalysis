from cProfile import label
from tkinter import scrolledtext
from unittest import result
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
from sklearn import tree
from sklearn.tree import export_text
import seaborn as sns

# Reading data
try:
    data=pd.read_csv(file_name_learning_data)
except:
    print("Error")
data.drop(columns=["Unnamed: 0","App_Id"],inplace=True)

le = preprocessing.LabelEncoder()
data["Category"]=le.fit_transform(data["Category"])
normalized_data=data.copy()
scalar=MinMaxScaler()
scalar.fit_transform(normalized_data)
normalized_data=pd.DataFrame(scalar.fit_transform(normalized_data) ,columns=normalized_data.columns)

def split_train_test_Learning_Price():
    X=normalized_data.drop(columns=["Price"]).copy()
    Y=normalized_data["Price"].copy()
    X_train, X_test, y_train, y_test =train_test_split(X,Y ,random_state=42)
    return X_train, X_test, y_train, y_test
    
# Price colunm as test group--> Using RandomForestRegressor Algorithem
def RandomForestRegressor_function():
    X_train, X_test, y_train, y_test =split_train_test_Learning_Price()
    Regressor_tree=RandomForestRegressor(n_estimators=100 , random_state=42)  
    Regressor_tree.fit(X_train,y_train)
    Regressor_tree_prediction = Regressor_tree.predict(X_test) # Make predictions for the test set
    mse = mean_squared_error(y_test, Regressor_tree_prediction)
    rmse = mse**0.5
    print("Mean squared error for Random Forest Regressor:",mse)
    print("Root of Mean squared error for Random Forest Regressor: ",rmse)
    print("Random Forest Regressor score",r2_score(y_test,Regressor_tree_prediction))
RandomForestRegressor_function()

# Price colunm as test group--> Using LinearRegression Algorithem
def LinearRegression_function():
    linear_tree=LinearRegression()
    X_train, X_test, y_train, y_test = split_train_test_Learning_Price()
    linear_tree.fit(X_train, y_train)
    linear_prediction = linear_tree.predict(X_test)
    print('Mean Squared Error for Linear Regression:', metrics.mean_squared_error(y_test, linear_prediction))
    print('Root Mean Squared Error for Linear Regression:', np.sqrt(metrics.mean_squared_error(y_test, linear_prediction)))
    print("LinearRegression score:",r2_score(y_test,linear_prediction))
LinearRegression_function()
# For Price colunm as test group, it's impossible to do confusion matrix because test group is continuous

#  Rating column as test group --> Using RandomForestClassifier
df_for_rating=data.copy()
df_for_rating["Rating"]=df_for_rating["Rating"].apply(lambda x: math.floor(x) if x + 0.5 == math.ceil(x) else round(x)) # Rounding rating column

def split_train_test_Learning_Rating():
    X=df_for_rating.drop(columns=["Rating"]).copy()
    Y=df_for_rating["Rating"].copy()
    X_train, X_test, y_train, y_test =train_test_split(X,Y ,random_state=42)
    return X_train, X_test, y_train, y_test

def RandomForestClassifier_function():
    X_train, X_test, y_train, y_test = split_train_test_Learning_Rating()
    forest=RandomForestClassifier(n_estimators=100, random_state=42) # practicing on 100 different trees
    forest.fit(X_train, y_train)
    y_pred = forest.predict(X_test)
    print("Accuracy score for Random Forest Classifier:",metrics.accuracy_score(y_test, y_pred))
    print("Cunfusion Matrix for Random Forest Classifier:\n",confusion_matrix(y_test,y_pred))
    tree_distribution=tree.export_text(forest.estimators_[0],feature_names=list(df_for_rating.drop(columns=["Rating"]).copy().columns)) # plotting the first tree
    print(tree_distribution)
    sns.heatmap(confusion_matrix(y_test,y_pred),annot=True, cmap='Blues',fmt=".1f") #plotting confusion matrix heatmap for RandomForestClassifier
    plt.title('Confusion Matrix for Random Forest Classifier')
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.show()
RandomForestClassifier_function()

## Conclusion from confusion matrix: The RandomForestClassifair Algorithem had problems classifying apps with rating between 0-1, because there isn't enough data regarding to apps with Rating of 1-0
## data contains only 23 apps below rating 2 --> total apps number is 725382

# Rating column as test group --> Using KNeighborsClassifier
def split_train_test_Normalization():
    X=df_for_rating.drop(columns=["Rating"]).copy()
    knn_df=pd.DataFrame(scalar.fit_transform(X),columns=X.columns) #normalizing the DataFrame without rating column
    knn_df["Rating"]=df_for_rating["Rating"].copy()
    X_train, X_test, y_train, y_test = train_test_split(knn_df.drop(columns=["Rating"]), knn_df["Rating"], test_size=0.25, random_state=42)
    return X_train, X_test, y_train, y_test

#  calculating error rate for N different neighbors 
def  KNN__Error_Rate_function(top_n):
    X_train, X_test, y_train, y_test =split_train_test_Normalization()
    error_rate = []
    for i in range(1,top_n):
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(X_train,y_train)
        pred_i = knn.predict(X_test)
        error_rate.append(np.mean(pred_i != y_test))
    print(error_rate)
    plt.figure(figsize=(10,6))
    plt.plot(range(1,36),error_rate,color='blue', linestyle='dashed', marker='o',markerfacecolor='red', markersize=10)
    plt.title('Error Rate vs. K Value')
    plt.xlabel('K')
    plt.ylabel('Error Rate')
KNN__Error_Rate_function(35)

def Best_KNN(best_n):
    X_train, X_test, y_train, y_test =split_train_test_Normalization()
    Knn_Classifier=KNeighborsClassifier(n_neighbors=best_n) # 3 Neighbors has the lowest error rate
    Knn_Classifier.fit(X_train,y_train)
    KNN_pred=Knn_Classifier.predict(X_test)
    print("KNN accuracy score:",metrics.accuracy_score(KNN_pred,y_test))
    print("Cunfusion Matrix for KNeighborsClassifier:\n",confusion_matrix(y_test,KNN_pred))
    sns.heatmap(confusion_matrix(y_test,KNN_pred),annot=True, cmap='Blues',fmt=".1f") # plotting confusion matrix heatmap for KNeighborsClassifier
    plt.title("Confusion Matrix for k-Nearest-Neighbor")
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.show()
Best_KNN(3)

#Rating column as test group--> Using SVM 
def SVM_function():
    X_train, X_test, y_train, y_test =split_train_test_Normalization()
    svm_classifier=svm.SVC(kernel="linear")
    svm_classifier.fit(X_train,y_train)
    y_pred=svm_classifier.predict(X_test)
    print("SVM accuracy score:",metrics.accuracy_score(y_test, y_pred))
SVM_function()    


