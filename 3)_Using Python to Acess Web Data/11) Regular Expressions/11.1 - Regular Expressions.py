# Regular Expressions
# a regular expression is a form of a language, and meaning it's a way to say that a set of strings match or don't match a regular expression.

#Understanding Regular Expressions

#Using re.search() Like find()
'''hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From') >= 0:
        print(line)

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line) : 
        print(line)'''


# Wild-Card Characters
'''   ^X.*:         '''
#      ^ is  Match the start of the line
#      . is any character. Match any character.
#      * is zero or more. Many times

'''    ^X-\S+ :     '''
#       \S is Match any non-whitespace character
#       + is One or more times


'''Python Regular Expression Quick Guide

^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times 
         (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times 
         (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end'''




