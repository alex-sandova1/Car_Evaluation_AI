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

#starts work on the OvR classifier
clf = OneVsRestClassifier(LogisticRegression())
clf.fit(X_train, y_train)
grid_values = {'estimator__C': [0.001, 0.01, 0.1, 1]}
grid_search = GridSearchCV(clf, param_grid=grid_values, cv=5)
grid_search.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# accuracy before tuning hyperparameters
print("Accuracy before tuning hyperparameters:", accuracy_score(y_test, y_pred))

###############################################################tune hyperparameters

#tune solver hyperparameter
clf = OneVsRestClassifier(LogisticRegression())
clf.fit(X_train, y_train)
grid_values = {'estimator__solver': ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga']}

grid_search = GridSearchCV(clf, param_grid=grid_values, cv=5)
grid_search.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# accuracy after tuning hyperparameters
print("Accuracy after tuning hyperparameters:", accuracy_score(y_test, y_pred))
