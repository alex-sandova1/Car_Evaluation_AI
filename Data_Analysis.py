import pandas as pd
from sklearn.model_selection import train_test_split

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

#store cars by number of doors
two_doors = data[data['doors'] == '2']
three_doors = data[data['doors'] == '3']
four_doors = data[data['doors'] == '4']
five_or_more_doors = data[data['doors'] == '5more']

#print cars by number of persons
print("Number of cars with 2 doors: " + str(len(two_doors)))
print("Number of cars with 3 doors: " + str(len(three_doors)))
print("Number of cars with 4 doors: " + str(len(four_doors)))
print("Number of cars with 5 or more doors: " + str(len(five_or_more_doors)))

#storew caers by number of persons
two_persons = data[data['persons'] == '2']
four_persons = data[data['persons'] == '4']
more_than_four_persons = data[data['persons'] == 'more']

#print cars by number of persons
print("Number of cars with 2 persons: " + str(len(two_persons)))
print("Number of cars with 4 persons: " + str(len(four_persons)))
print("Number of cars with more than 4 persons: " + str(len(more_than_four_persons)))

#



