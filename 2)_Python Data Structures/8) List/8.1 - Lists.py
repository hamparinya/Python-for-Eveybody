# Algorithms

# A list is a Kind of Collectiohs
# A collection allows us to put many values in a single "variable"
# ans It is nice because we can carry many values around in one convinient package
friends = ['Joseph', 'Glenn', 'Sally']
#              ^        ^        ^
#              0        1        2
carryn = ['socks', 'shirt', 'perfume']

#List Constants 
print([1, 24, 76]) # in () is a strings -> [1, 24, 76]
print(['red','yellow','blue'])  #-> ['red', 'yellow', 'blue']
print([1, [5,6], 7])  #-> [1, [5,6], 7]
print([])           #-> []


#List and Definite Loops - Best Pals
z = friends
for x in z:
    print('Happy New Year:', x)
print('Done!')

#Looking Inside Lists
print(z[1])

#Lists Are Mutable
fruit = 'Banana'
#fruit[0] = 'b' It will not print out because it not allow to change the strings
x = fruit.lower() # best way to change
print(x)
lotto = [2, 14, 26, 41, 63]
print(lotto)
lotto[2] = 28 # integer
print(lotto)

#How Long is a List?
greet = 'Hello Bob'
print(len(greet)) #Length counts a Spacebar
K = [1, 2, 'joe', 99] #for ' ' in list, Length will be counted as one (interger)
print(len(K))

#Using the Range Function
print(range(4))             #-> [0, 1, 2, 3]
print(len(friends))         #-> 3
print(range(len(friends)))  #-> [0, 1, 2]

#A Tale of two Loops 
for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year:', friend)



