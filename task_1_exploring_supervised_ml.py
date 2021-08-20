# -*- coding: utf-8 -*-
"""TASK-1 -  Exploring Supervised ML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zO8187h24rDRb6dxFm6vrSVCfd90DjJL

##Name : B Sri Sai Vijitha

#TASK-1

##Predict the percentage of an student based on the no. of study hours.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path="http://bit.ly/w-data"
data=pd.read_csv(path)
data

data.head()

"""###Discover and visulaize the data to gain insigths

"""

data.info()

data.describe()

plt.scatter(x=data.Hours,y=data.Scores)
plt.xlabel("Study Hours")
plt.ylabel("Study Time")
plt.title("Study Hours Vs Student Marks ")
plt.show()

"""###Prepare The Data For Machine Learning Algorithm

#### #data cleaning
"""

data.isnull().sum()

# split dataset for training
x=data.drop("Scores", axis="columns")
y=data.drop("Hours",axis="columns")
print("shape of x",x.shape)
print("shape of y", y.shape)

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.6, random_state=51)
 # tes_size is defining how much data we want for testing so 0.6 means i am using 20 percent data for testing

print("shape of X Train",X_train.shape)
print("shape of Y Train",Y_train.shape)
print("shape of X Test", X_test.shape)
print("shape of Y Test",Y_test.shape)

"""###Select a model and train it

"""

# So in above scatter plot as we saw that when the value of x is increasing the value of y is also increasing in a linear format so we can use linear regression model
from sklearn.linear_model import LinearRegression
lr=LinearRegression()

lr.fit(X_train,Y_train)

lr.coef_

lr.intercept_

lr.predict([[4]])[0][0].round(2)

y_pred=lr.predict(X_test)
y_pred

pd.DataFrame(np.c_[X_test,Y_test,y_pred], columns=["Hours","Scores_original","Scores_predicted"])

