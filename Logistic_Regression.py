import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
data = pd.read_csv('car.data', names=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class'])

# Prepare the data
X = data[['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety']]
y = data['class']
#display X data
#print(X) #shows that data was read correctly

#split into training, validation and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25)

#convert string data to numerical data
X_train = pd.get_dummies(X_train)
X_test = pd.get_dummies(X_test)
X_val = pd.get_dummies(X_val)

#fit the model
model = LogisticRegression()
model.fit(X_train, y_train)

#predict the model
y_pred = model.predict(X_val)

#evaluate the model
score = model.score(X_val, y_val)
print(score)

#test the model
y_pred = model.predict(X_test)
score = model.score(X_test, y_test)
print(score)

#tune C parameter using GridSearchCV
parameters = {'C': [0.001, 0.01, 0.1, 1]}
clf = GridSearchCV(model, parameters, cv=5)
clf.fit(X_train, y_train)
print(clf.best_params_)
print(clf.best_score_)
print(clf.score(X_test, y_test))

#tune penalty parameter using GridSearchCV
parameters = {'penalty': ['l1', 'l2']}
clf = GridSearchCV(model, parameters, cv=5)
clf.fit(X_train, y_train)
print(clf.best_params_)
print(clf.best_score_)
print(clf.score(X_test, y_test))



