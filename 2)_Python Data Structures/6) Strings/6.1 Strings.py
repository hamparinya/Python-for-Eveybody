#Strings Data Type
str1 = 'Hello'
str2 = "there"
bob = str1 + str2
print(bob)

str3 = '123'
'''str3 = str3 + 1''' #จะไม่ขึ้นถ้ายังไม่เปลี่ยน  convet (' ') to be int or float
x = int(str3) + 1 #Convert Str to be Int
print(x)

# Reading and Converting
name = input("Name : ") #Typing some Name
print(name)
num = input("Number :")
'''x = num - 10''' # Num is Str, It will do not print out. Should Convert Str to be int or float first.
x = int(num) - 10
print (x)

# Looking Inside strings
''' b a n a n a
    0 1 2 3 4 5 '''
fruit = 'banana'
letter = fruit[1]
print(letter)       #-> a
x = 3
w = fruit[x-1]
print(w)            #-> n
# if a characrter is too far, It will do not print out
''' zot = 'abc'
    print(zot[5])''' #this line is wrong. because str is too shrot than order, that jut 3 not 5

#Strings have length
''' b a n a n a
    0 1 2 3 4 5 
    But It is couanted 6'''
fruit = 'banana'
x = len(fruit)
print(x)            #-> 6

#Looping Through strings
fruit = 'banana'
index = 0
while index < len(fruit):  # It means index is equal or monre than len(fruite) that be False, It will no be loop again.
    letter = fruit[index]
    print(index, letter)   # remove a index, It will be the same as below conditon
    index = index + 1      # 4 line needed, delete 1
for letter in fruit :      # This condition is shoeter than above .
    print(letter)          # 2 Line needed

# Looping and Counting
word = 'Banana'
count = 0
for letter in word :
    if letter == 'a':
        count = count + 1
print(count)

#Slicing Strings
s = 'Monty Python'
print(s[0:4])
print(s[6:20])
print(s[:])
