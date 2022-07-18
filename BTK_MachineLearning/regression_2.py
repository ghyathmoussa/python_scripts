''' 
    - just to save model
    - the file not work perfectly
'''

import pandas as pd
import numpy as np

data = pd.read_csv('eksikveriler.csv')

c = data.iloc[:,-1:].values
print(c)

from sklearn import preprocessing

le = preprocessing.LabelEncoder()

c[:,-1] = le.fit_transform(data.iloc[:,-1])

ohe = preprocessing.OneHotEncoder()

c = ohe.fit_transform(c).toarray()

print(c)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
# regressor.fit(x_train,y_train)

# y_pred = regressor.predict(x_test)

""" Usage of Statsmodel Laibrary """

import statsmodels.api as sm

X = np.append(arr=np.ones((22,1)).astype(int), values=data, axis=1)

