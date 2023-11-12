from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
import pandas as pd

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

#start with default parameters
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

#predict the model
y_pred = model.predict(X_val)

#evaluate the model
score = model.score(X_val, y_val)
#print(score)

#tune max_depth parameter using GridSearchCV
parameters = {'max_depth': [2, 4, 6, 8, 10]}
clf = GridSearchCV(model, parameters, cv=5)
clf.fit(X_train, y_train)
print(clf.best_params_)
print(clf.best_score_)
print(clf.score(X_test, y_test))

print(" ")

#tune min_samples_split parameter using GridSearchCV
parameters = {'min_samples_split': [2, 4, 6, 8, 10]}
clf = GridSearchCV(model, parameters, cv=5)
clf.fit(X_train, y_train)
print(clf.best_params_)
print(clf.best_score_)  
print(clf.score(X_test, y_test))

#evaluate the model
score = model.score(X_test, y_test)
#print(score)

