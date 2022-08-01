import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# data preprocessing
data = pd.read_csv('../maaslar_yeni.csv')

# x = data.iloc[:,2:3].values
x = data.iloc[:,2:5].values # cause to overfit
y = data.iloc[:,5:].values

# Linear regression
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x,y)

# plt.scatter(x,y,color='red')
# plt.plot(x,lin_reg.predict(x))
# plt.show()

import statsmodels.api as sm
model = sm.OLS(lin_reg.predict(x),x)
print(model.fit().summary())

# Polynomial Regression
from sklearn.preprocessing import PolynomialFeatures
lin_pol = PolynomialFeatures(degree=4)
x_poly = lin_pol.fit_transform(x)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,y)
print('\n############ Poly OLS ############\n')
model2 = sm.OLS(lin_reg2.predict(lin_pol.fit_transform(x)),x)
print(model2.fit().summary())