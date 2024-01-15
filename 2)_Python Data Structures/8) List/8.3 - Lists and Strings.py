#Best Friends: Strings and Lists
abc = 'With three words'
stuff = abc.split() # .split() will seperate between and word
print(stuff)
print(len(stuff))   #->3
print(stuff[0])     #-> With
for w in stuff :
    print(w)

line = 'first;second;third'
thing = line.split()
print(thing)
print(len(thing))

thing = line.split(';')  # add ';' to split the word
print(thing)
print(len(thing))

'''fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.splitlines('From '):
        continue
    word = line.split()
    print(word[2])'''       


# The Double Split Pattern
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = x.split()
email = words[1]
print(email)
pieces = email.split('@')
print(pieces)




