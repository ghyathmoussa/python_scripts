from matplotlib.cm import ScalarMappable
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

""" Data preperation """
data = pd.read_csv('../maaslar.csv')

x = data.iloc[:,1:2]
y = data.iloc[:,2:]

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
x_sc = sc.fit_transform(x)
y_sc = sc.fit_transform(y)

from sklearn.svm import SVR

svr = SVR(kernel='rbf')
svr.fit(x_sc,y_sc)

plt.scatter(x_sc,y_sc)
plt.plot(x_sc,svr.predict(x_sc))
plt.show()