#Tuples are Like Lists
x = ('Glen', 'Sally', 'Joseph')
print(x[2])
y = (1, 9, 2)
print(max(y))

for iter in y:
    print(iter)


# but Tuples are "immutable" You cannot alter its contents - similar to a string
x = [9, 8, 7]  #Integer in list 
x[2] = 6
print(x)

y = 'ABC' #string
# y[2] = 'D'    Traceback: str' object does not support item assignment

z = (5, 4, 3) #tuple
# z[2] = 0      Traceback: tuple' object does not support item assignment


#Things not to do With Tuples
# x.sort() x.append() x.reverse is not used in Tuples
l = list()               
print(dir(l))   # 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
t = tuple()     
dir(t)          # Tuples can use .count() and .index()

#Tuples Are More effienct for "temporary variables" we prefer tuples over lists

#Tuples and Assigment
(x, y) = (4, 'fred')
print(y)    #-> fred
(a, b) = (99, 98)
print(a)    #-> 99

#Tuples and Dictionaries
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print(k, v)

tups = d.items()
print(tups)

#Tuples are Comparable
print ((0, 1, 2) < (5, 1, 2))
print((0, 1, 200000) < (0, 3, 4))

#Sorting Lists of Tules
d = {'a': 10, 'b':1, 'c':22}
print(d.items())
print(sorted(d.items()))

#Using sorted()
t = sorted(d.items())
print(t)
for k,v in t:
    print(k,v)  #keys and values

#Sort by Values Instead of Key
c = {'a': 10, 'b':1, 'c':22}
tmp = list()
for k, v in c.items():
    tmp.append((v, k))
print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)

#Even Shoter Version
c = {'a': 10, 'b':1, 'c':22}
print( sorted( [ (v,k) for k,v in c.items()  ]  )  )

# The top 10 most common words
fhand = open('rome.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 1) + 1
lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
for val, key in lst[:10]:
    print(key,val)

