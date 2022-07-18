from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('maaslar.csv')

x = data.iloc[:, 1:2]
y = data.iloc[:,2:]

""" Linear Regression model"""
from sklearn.linear_model import LinearRegression
lr = LinearRegression()

# lr.fit(x,y)
# plt.scatter(x,y,color='red')
# plt.plot(x,lr.predict(x))

# plt.show()

""" ploynomial regression model """
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=4)
x_poly = poly_reg.fit_transform(x)
print(x_poly)

lr.fit(x_poly,y)
plt.scatter(x,y,color='red')
plt.plot(x,lr.predict(poly_reg.fit_transform(x)))
plt.show()