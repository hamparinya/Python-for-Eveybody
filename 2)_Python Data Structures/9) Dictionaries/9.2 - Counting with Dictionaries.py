#Many Counters with a Dicrionary
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)

# Dictionary Tracebacks
''' print(ccc['csev']) '''  # It will be error Tracebacks
print ('csev' in ccc )

#When We See a New Name
counts = dict()         #----> (1)
names = ['csev', 'cwen', 'csev', 'sqian', 'cwen'] #--->(2)
for name in names :
    if name not in counts :
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)

# The get Method for Dictionaries 
if name in counts:
    x = counts[name]
else :
    x = 0
x = counts.get(name, 0)

#simplified Counting with get()
x = dict()
Hams = ['Man U', 'Liverpoo', 'Chelsea', 'Man City', 'Spur', 'Arsenal', 'Man U'] 
for Ham in Hams :
    x[Ham] = x.get(Ham, 0) + 1
print(x)




