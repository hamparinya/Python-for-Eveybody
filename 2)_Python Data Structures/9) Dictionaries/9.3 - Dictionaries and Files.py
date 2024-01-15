#Counting Pattern
from os import spawnl


counts = dict()
line = 'the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car'
#line = input('Enter a line of text :')
words = line.split()
print('words:', words)
print('Counting...')

for word in words:
    counts[word] = counts.get(word, 0) + 1
print('counts: ', counts)

#Definte Loops and Dictionaries
groups = { 'chuck': 1, 'fred': 42, 'jan':100}
for key in groups:
    print(key, groups[key])

# Retrieving lists of Keys and Values 
jjj = { 'chuck': 1, 'fred': 42, 'jan':100 }
print(list(jjj))
k = jjj.keys()
print(k)       #->['chuck', 'fred', 'jan'] , It called Key
v = jjj.values()
print(v)     #->[1, 42, 100]  It called  value
i = jjj.items()
print(i)      #->[('chuck', 1), ('fred', 42), ('jan', 100)]
                        #   ^          ^
                        #            Tuple    

#Bonus: Two Iteration Variables!
for aaa,bbb in jjj.items():
    print(aaa,bbb)
    #   aaa    bbb
    #  [jan]    100
    # [chunk]   1
    #  [fred]   42

#Top code
name = input('Enter file:   ')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or counts > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)