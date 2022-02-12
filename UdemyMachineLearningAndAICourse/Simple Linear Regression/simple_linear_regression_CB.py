# Simple Linear Regression

#DATA PREPROCESSING
import numpy as mp 
import matplotlib.pyplot as plt 
import pandas as pd

#importing the dataSet
dataset =pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,1].values

#Split to training and test set

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size = 1/3,random_state = 0)

#Feature Scaling

""""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""


#Fitting Simple Linear Regression to training set
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train,Y_train)

#Predicting the test set values
Y_pred = regressor.predict(X_test)

#Training Set Visuals
#plt.scatter(X_train,Y_train,color ='red')
#plt.plot(X_train,regressor.predict(X_train),color ='blue')
#plt.title('Salary V Exp (Training Set)')
#plt.xlabel('Years')
#plt.ylabel('Salary')
##plt.savefig('foo.png')
#plt.show()
#Test Set Visuals
plt.scatter(X_test,Y_test,color ='red')
plt.plot(X_train,regressor.predict(X_train),color ='blue')
plt.title('Salary V Exp (Test Set)')
plt.xlabel('Years')
plt.ylabel('Salary')
#plt.savefig('foo.png')
plt.show()