#Concatenating Lists Using +
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)    [1, 2, 3, 4, 5, 6]

#Lists Can Be Sliced Using:
t = [9, 41, 12, 3, 74, 15]
print(t[1:3])   #-> [41, 12]
print(t[:4])    #-> [9, 41, 12, 3]
print(t[3:])    #-> [3, 74, 15]
print(t[:])     #-> [9, 41, 12, 3, 74, 15]

#List Methods
x = list()
print(type(x)) 
dir(x)

#Building a List from Scracth
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)    #-> ['book', 99]
stuff.append('cookie')
print(stuff)    #-> ['book', 99, 'cookie']

#Is Something in a List?
some = [1, 9, 21, 10, 16]
print(9 in some)  #-> True
print(15 in some) #-> False
print(20 not in some) #-> True

#Lists are in Order
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)  #->['Glenn', 'Joseph', 'Sally']
print(friends[1]) #->Joseph

#Built-in Functions and Lists
nums = [3, 41, 12 , 9, 74, 15]
print(len(nums)) #-> 6u
print(max(nums)) #-> 74
print(min(nums)) #-> 3
print(sum(nums)) #-> 154
print(sum(nums)/len(nums)) #-> 25.6

#Old way
total = 0
count = 0
while True :
    s = input('Enter a number: ') #type 3, 9, 5 and done
    if s == 'done' : 
        break
    value = float(s)
    total = total + value
    count = count + 1
average = total/count
print('Average :', average)

#Call function
numlist = list()
while True:
    u = input('Enter a number: ')
    if u == 'done':
        break
    v = float(u)
    numlist.append(v)
av = sum(numlist)/len(numlist)
print('Average :', av)


