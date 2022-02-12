import numpy as mp 
import matplotlib.pyplot as plt 
import pandas as pd

#importing the dataSet
dataset =pd.read_csv('50_Startups.csv')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,4].values

#Categorical Varibles
from  sklearn.preprocessing import LabelEncoder , OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,3]=labelencoder_X.fit_transform(X[:,3])
onehotencoder = OneHotEncoder(categorical_features=[3])
X= onehotencoder.fit_transform(X).toarray();
#Remove the first row
X= X[:,1:]


#Split to training and test set

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size = 0.2,random_state = 0)

#Feature Scaling
""""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""


#Fit Multi Linear Regression to Training Set

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train,Y_train)

#predicting the test set result
Y_pred=regressor.predict(X_test)


#Using Backward Elimnation 
import statsmodels.formula.api as sm
X = mp.append(arr= mp.ones((50,1)).astype(int),values=X,axis = 1)
X_opt = X[:,[0,1,2,3,4,5]]
regressor_OLS = sm.OLS(endog= Y,exog=X_opt).fit()
regressor_OLS.summary()

X_opt = X[:,[0,1,3,4,5]]
regressor_OLS = sm.OLS(endog= Y,exog=X_opt).fit()
regressor_OLS.summary()

X_opt = X[:,[0,3,4,5]]
regressor_OLS = sm.OLS(endog= Y,exog=X_opt).fit()
regressor_OLS.summary()

X_opt = X[:,[0,3,5]]
regressor_OLS = sm.OLS(endog= Y,exog=X_opt).fit()
regressor_OLS.summary()

X_opt = X[:,[0,3]]
regressor_OLS = sm.OLS(endog= Y,exog=X_opt).fit()
regressor_OLS.summary()




#predicting the test set result
X_test = mp.append(arr= mp.ones((10,1)).astype(int),values=X_test[:,[2]],axis = 1)
Y_pred_OLS=regressor_OLS.predict(X_test)