import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ########### preparing data ###########
data = pd.read_csv('../data/veriler.csv')

x = data.iloc[:,1:4].values
y = data.iloc[:,4:].values

""" ########### Splinting data ########### """
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.33,random_state=0)

""" ########### Scaling data ########### """

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

X_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)

""" ########### Model ########### """
from sklearn.linear_model import LogisticRegression
log_r = LogisticRegression(random_state=0)
log_r.fit(x_train,y_train)

pred = log_r.predict(x_test)
print(y_test)
print(pred)
# confusion matrixs
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,pred)

print(cm)