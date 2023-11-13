import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score 

# Read the data
data = pd.read_csv('car.data', names=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class'])

# Prepare the data
X = data[['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety']]
y = data['class']

#split into training, validation and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25)

#convert string data to numerical data
X_train = pd.get_dummies(X_train)
X_test = pd.get_dummies(X_test)
X_val = pd.get_dummies(X_val)

clf = OneVsRestClassifier(LogisticRegression())
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("Accuracy score: ", accuracy_score(y_test, y_pred))
print(" ")

#tune C parameter using GridSearchCV
parameters = {'estimator__C': [0.001, 0.01, 0.1, 1]}
clf = GridSearchCV(clf, parameters, cv=5)
clf.fit(X_train, y_train)
print(clf.best_params_)
print(clf.best_score_)
print(clf.score(X_test, y_test))
print(" ")

#tune penalty parameter using GridSearchCV
parameters = {'estimator__penalty': ['l1', 'l2']}
clf = GridSearchCV(clf, parameters, cv=5)
clf.fit(X_train, y_train)
print(clf.best_params_)
print(clf.best_score_)
print(clf.score(X_test, y_test))
print(" ")

