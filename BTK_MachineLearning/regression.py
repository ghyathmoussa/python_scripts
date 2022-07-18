from winsound import PlaySound
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('satislar.csv')

# print(data.head())
aylar = data[['Aylar']]
satislar = data[['Satislar']]

# Prepare Data
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

x_train,x_test,y_train,y_test = train_test_split(aylar,satislar,test_size=0.3,random_state=0)

sc = StandardScaler()

# x_train = sc.fit_transform(x_train)
# x_test = sc.fit_transform(x_test)

# y_train = sc.fit_transform(y_train)
# y_test = sc.fit_transform(y_test)

# Model
from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(x_train,y_train)

model = lr.predict(x_test)

x_train = x_train.sort_index()
y_train = y_train.sort_index()

plt.scatter(x_train,y_train)
plt.plot(x_test,model)
plt.show()
