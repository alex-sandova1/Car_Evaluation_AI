import pandas as pd
import matplotlib.pyplot as plt

#store fdg data in a dataframe
data = pd.read_csv('car.data', names=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class'])

#check for zero or null values
print(data.isnull().sum())

#check for duplicate data
dups = data.duplicated().sum()
print("Number of duplicate rows: ", dups)

#count number of vgood, good, acc, unacc
print(data['class'].value_counts())

#display data in a pie chart
data['class'].value_counts().plot(kind='pie', autopct='%1.0f%%', colors=['red', 'green', 'blue', 'yellow'])
plt.title('Class Distribution')
plt.show()






