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
X_test = sc.fit_transform(x_test)

""" ########### Model ########### """
from sklearn.neighbors import KNeighborsClassifier
# confusion matrixs
from sklearn.metrics import confusion_matrix

knn = KNeighborsClassifier(n_neighbors=1,metric='minkowski')

knn.fit(X_train,y_train)

pred = knn.predict(X_test)
print(pred)
cm = confusion_matrix(y_test,pred)
print(cm)