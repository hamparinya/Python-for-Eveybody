import re

hand  = open('regex_sum_1002552.txt')
numlist = []
for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    if len(stuff) < 1 :continue #skip number that no have a length
    
    for i in stuff:         
        num = float(i)
        numlist.append(num)

''' for i in range(len(stuff)):   It's so the same way
        num = float(stuff[i])
        numlist.append(num)     '''
   
print('The sum for the sample text above is ', sum(numlist))
