import pandas as pd


#check for null values in data
data = pd.read_csv('car.data', names=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class'])
print(data.isnull().sum())

#check for 0 values in data
print((data[['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']] == 0).sum())

#while loop to go through data and check for bad deals
i = 0
while i < len(data):
    if data['buying'][i] == 'vhigh': 
        if data['maint'][i] == 'vhigh' or data['maint'][i] == 'high':
            print("car #", [i], " is a bad deal")
        elif data['maint'][i] == 'med' and data['safety'][i] == 'high':
            print("car #", [i], " is an acceptable deal")
        elif data['maint'][i] == 'low' and data['safety'][i] == 'high' and data['lug_boot'][i] == 'big':
            print("car #", [i], " is an acceptable deal")
        elif data['maint'][i] == 'low' and data['safety'][i] == 'med' and (data['lug_boot'][i] == 'med' or data['lug_boot'][i] == 'big') and (data['doors'][i] == '2' or data['doors'][i] == '3' or data['doors'][i] == '4'):
            print("car #", [i], " is an acceptable deal")
    elif data['buying'][i] == 'high':
        if data['maint'][i] == 'vhigh':
            print("car #", [i], " is a bad deal")
        elif data['maint'][i] == 'high':
            if data['safety'][i] == 'high' and data['persons'][i] == '4':
                print("car #", [i], " is an acceptable deal")
            elif data['safety'][i] == 'high' and data['persons'][i] == 'more':
                print("car #", [i], " is an acceptable deal")
            elif data['safety'][i] == 'med' and (data['lug_boot'][i] == 'big' or (data['lug_boot'][i] == 'med' and data['person'][i] == 'more')):
                print("car #", [i], " is an acceptable deal")
        elif data['buying'][i] ==  'med':
            
            
            
        
        
    else:
        print("car #", [i], " is a bad deal")
    i = i + 1