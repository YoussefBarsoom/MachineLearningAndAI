
import numpy as mp 
import matplotlib.pyplot as plt 
import pandas as pd

#importing the dataSet
dataset =pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:2].values
Y = dataset.iloc[:,2].values

#Split to training and test set
#from sklearn.model_selection import train_test_split
#X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size = 0.2,random_state = 0)

#Feature Scaling

""""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""


#Fit Decision Tree Regression to the dataset
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X,Y)
#Predict result w/ Polynomial Reg
y_pred=regressor.predict([[6.5]])

#Visuals for Polynomial 

#plt.scatter(X,Y,color= 'green')
#plt.plot(X,regressor.predict(X),color='blue')
#plt.title('Decision Tree Regression Presentation')
#plt.show()

#higher resolution
X_grid = mp.arange(min(X),max(X),0.01)
X_grid = X_grid.reshape((len(X_grid)),1)
plt.scatter(X,Y,color= 'green')
plt.plot(X_grid,regressor.predict(X_grid),color='blue')
plt.title('Decision Tree Regression Presentation')
plt.show()





