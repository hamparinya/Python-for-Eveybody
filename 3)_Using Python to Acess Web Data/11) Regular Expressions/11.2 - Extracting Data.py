# Matching and Extracting Data
# research returns a True/False depending on wheather the string matches the regular expressions
# If we actually want the matching strings to be extracted, we use re.fingall()

import re
x = ' My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)          # + is one or more digits

k = re.findall('[AEIOU]+', x)
print(k)        # AEIOU did not found 


#Warning : Greedy Matching
import re
x = 'From: Using the : character'
y = re.findall('^F.+:',x)
print(y)       # It will take the big thing

# Non-Greedy Matching  
# If you add a ? character, the + and ^ chill out a bit..
import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)

#Fine-Tuning String Extraction
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
                        # ^         ^ 
                        # 21        31
y = re.findall('\S+@\S+', x)
print(y)        # \S+ is at least one non-white space chracter.
                # @ is Character.
# Parentheses are not part of the match 
y = re.findall('^From.(\S+@\S+)', x)
print(y)               # ( ) they tell where to start an stop what string to extract

atpos = x.find('@')
print(atpos)        # string slice at 21

sppos = x.find(' ', atpos)
print(sppos)        # string slic at 31

host = x[atpos+1 :sppos]
print(host)

# The double split Pattern
word = x.split()
email = word[1]
print(email)
piece = email.split('@')
print(piece)
print(piece[1])
# The Regex Version
import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
l = re.findall('@([^ ]*)', lin) #[^ ] Match non-blank character, * Match many of them
            # or ^From .*@[^ ]*  # That mean Starting at the bgining of line , look the string 'From'
print(l)

# Spam Confidence
'''import re
hand  = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence :([0-9.]+)', line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximun:', max(numlist))'''

# Escape Character   use fixed with \
import re
x = 'We just received $10.00 for cookies'
y = re.findall('\$[0-9.]+', x)
print(y)  


