# List = A linear collection of values that stay in order.
# Dictionary = A "bag" of value, each with its own label.

#Dictionaries
purse = dict() #purse = virable of dictonary
purse['money'] = 12 # 12 put into purse and lebel is 'money'
purse['candy'] = 3
purse['tissue'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2  # To 2 was added with 3
print(purse)    #-> {'money': 12, 'candy': 5, 'tissue': 75} 

#Conparing Lists and Dictionaries
lst = list()
lst.append(21)  # add into positon 0
lst.append(183) # add into positon 1
print(lst)
lst[0] = 23     # change 21 to be 23
print(lst)

ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)
ddd['age'] = 23   # change 21 to be 23
print(ddd)


#Dictionary Literals(Constants)  'key' : value
jjj = {'chuck': 1 , 'fred' : 42, 'jan':100}
print(jjj)
ooo = {}
print(ooo)


