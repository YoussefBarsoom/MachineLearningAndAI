import numpy as mp 
import matplotlib.pyplot as plt 
import pandas as pd

#importing the dataSet
dataset =pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:2].values
Y = dataset.iloc[:,2].values


# Fit Linear Regression

from sklearn.linear_model import LinearRegression
linReg = LinearRegression()
linReg.fit(X,Y)

#Fit Polynomial Regression

from sklearn.preprocessing import PolynomialFeatures

poly_reg = PolynomialFeatures(degree=7)
X_poly = poly_reg.fit_transform(X)
linReg2 = LinearRegression()
linReg2.fit(X_poly,Y)

#Visuals for Linear 
plt.scatter(X,Y,color= 'green')
plt.plot(X,linReg.predict(X),color='red')
plt.title('Linear Presentation')
plt.show()
#Visuals for Polynomial 
X_grid = mp.arange(min(X),max(X),0.1)
X_grid = X_grid.reshape((len(X_grid)),1)
plt.scatter(X,Y,color= 'green')
plt.plot(X_grid,linReg2.predict(poly_reg.fit_transform(X_grid)),color='blue')
plt.title('Polynomial Presentation')
plt.show()


#Predict result w/ Linear Reg
linReg.predict([[6.5]])
#Predict result w/ Polynomial Reg
linReg2.predict(poly_reg.fit_transform([[6.5]]))









#Split to training and test set
#from sklearn.model_selection import train_test_split
#X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size = 0.2,random_state = 0)

#Feature Scaling

""""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""

