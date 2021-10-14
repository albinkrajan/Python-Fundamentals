str1 = "pythonista"
str2 = "The name is Albin K Rajan"
str3 ="1, 2, 3, 4"
#indexing
print(str1[1])
print(str1[-1])                 #negative indexing
#string slicing
print(str2[0:7])
print(str2[0:14:2])            #back propagation
print(str2[::-1])
#eg operations
print(len(str1))                #to find the length
print(str1.upper())             #convertion to upper
print(str1.lower())
print(str1.capitalize())        #capitalizes the first letter
print(str1.count("p"))
print(str1.isalnum())
print(str1.replace("p", "a"))    #old value & new value
print(str1.split("i"))
print(str1+str2)
