import re
from turtle import color
from matplotlib.cm import ScalarMappable
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import rand

""" Data preperation """
data = pd.read_csv('../maaslar.csv')

x = data.iloc[:,1:2]
y = data.iloc[:,2:]

""" Model """
from sklearn.tree import DecisionTreeRegressor

reg_dt = DecisionTreeRegressor(random_state=0)

reg_dt.fit(x,y)

plt.scatter(x,y,color='red')
plt.plot(x,reg_dt.predict(x))
# plt.show()
print(reg_dt.predict([[11]]))

""" Random Forest """
from sklearn.ensemble import RandomForestRegressor
reg_rf = RandomForestRegressor(random_state=0,n_estimators=10)
reg_rf.fit(x,y)

print(reg_rf.predict([[6.6]]))

plt.scatter(x,y,color='red')
plt.plot(x,reg_rf.predict(x),color='green')
# plt.show()

""" R2 Score """
""" To evaluate the model by R2 square """
""" Can be used in every model evaluation """
from sklearn.metrics import r2_score

print(r2_score(y,reg_rf.predict(x)))
