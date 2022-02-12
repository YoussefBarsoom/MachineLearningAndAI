

import numpy as mp 
import matplotlib.pyplot as plt 
import pandas as pd

#importing the dataSet
dataset =pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:2].values
Y = dataset.iloc[:,2:3].values

#Split to training and test set
#from sklearn.model_selection import train_test_split
#X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size = 0.2,random_state = 0)

#Feature Scaling

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X = sc_X.fit_transform(X)
sc_Y = StandardScaler()
Y = Y.reshape(-1, 1) 
Y = sc_Y.fit_transform(Y)

#Fit  Regression Model to the datase
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X,Y)

#Predict result w/ SVR Reg
#y_pred=regressor.predict([[6.5]])
y_pred=sc_Y.inverse_transform(regressor.predict(sc_X.transform(mp.array([[6.5]]))))
#Visuals for SVR 

plt.scatter(X,Y,color= 'green')
plt.plot(X,regressor.predict(X),color='blue')
plt.title('SVR Presentation')
plt.show()

#higher resolution

X_grid = mp.arange(min(X),max(X),0.1)
X_grid = X_grid.reshape((len(X_grid)),1)
plt.scatter(X,Y,color= 'green')
plt.plot(X_grid,regressor.predict(X_grid),color='blue')
plt.title('SVR Presentation')
plt.show()




