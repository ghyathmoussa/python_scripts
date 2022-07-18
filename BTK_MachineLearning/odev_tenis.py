import statsmodels.api as sm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

""" Main varaibles"""
data = pd.read_csv('odev_tenis.csv')
le = LabelEncoder()
"""
## End Main Variables


## Transform categorical data 

play = data.iloc[:,-1:].values
play[:,-1] = le.fit_transform(data.iloc[:,-1])

windy = data.iloc[:,-2:-1].values
windy[:,-1] = le.fit_transform(data.iloc[:,-1])
print(windy)

"""
""" Tranform Categorical Data """

data2 = data.apply(LabelEncoder().fit_transform)

x = data2.iloc[:, :1]

ohe = OneHotEncoder()

x = ohe.fit_transform(x).toarray()

weather_status = pd.DataFrame(data=x, columns=['over', 'rainy', 'sunny'])

final_data = pd.concat([weather_status, data.iloc[:, 1:3]], axis=1)

final_data = pd.concat([final_data, data2.iloc[:, -2:]], axis=1)

""" split data to train and test """

x_train, x_test, y_train, y_test = train_test_split(final_data.iloc[:, :-1], final_data.iloc[:, -1:], test_size=0.33,)

lr = LinearRegression()
lr.fit(x_train, y_train)

prediction = lr.predict(x_test)

for i in range(len(prediction)):
    if prediction[i] > 0.5:
        prediction[i] = 1
    else:
        prediction[i] = 0

# print(prediction)

""" 
    - Calculate the P-value
    - backward elimination 
"""


X = np.append(arr=np.ones((14, 1)).astype(int), values=final_data.iloc[:, :-1], axis=1)

left = final_data.iloc[:,:3]
right = final_data.iloc[:,4:]

final_data = pd.concat([left,right],axis=1)

print(final_data)
X_l = final_data.iloc[:,[0,1,2,3,4]].values

X_l = np.array(X_l,dtype=float)
model = sm.OLS(final_data.iloc[:,-1:],X_l).fit()
print(model.summary())


x_train, x_test, y_train, y_test = train_test_split(final_data.iloc[:, :-1], final_data.iloc[:, -1:], test_size=0.33,)
lr.fit(x_train,y_train)

prediction = lr.predict(x_test)

for i in range(len(prediction)):
    if prediction[i] > 0.5:
        prediction[i] = 1
    else:
        prediction[i] = 0

print(prediction)