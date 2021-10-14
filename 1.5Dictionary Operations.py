dict1 = {1: "pythonista", 2: "Albin K Rajan","third": "Python"}
dict2 = dict({1: 'Python', 2: 'Machine Learning'})
dict3  = {3: 'Cars', 4: 'Motorcycles', 6: 'Cycles', 7: 'Trucks'}
print(dict1)
print(dict2)
print(dict3)
print(dict1[1])
print(dict1.get(1))            #get function
print(dict1.get('third'))
dict2['third'] = 'A I'         #adding new value
#keys & values function
print(dict2.keys())
print(dict2.values())
#changing values
print(dict2)
dict2[5]='scikit learn'
print(dict2)
#deleting values
print(dict3.pop(3))
print(dict3.popitem())
del dict3[4]
print(dict3)



