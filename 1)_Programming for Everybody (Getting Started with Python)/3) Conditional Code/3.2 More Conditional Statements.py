# Visualize Blocks
x = 4
if x > 2 :
    print('Bigger')
else :
    print('Smaller')
print('All done')

#Multi-way
x =int(input('Enter the number : '))
if x < 2 :
    print('Smaller')
elif x < 10 :
    print('Medium')
elif x < 20 :
    print('Big')
elif x < 100 :
    print('Giant')
else :
    print('Large')
print('All done')

# The try and expept structure
astr = 'Bob'
try:
    print('Hello')
    istr = int(astr)
    print('There')
except:
    istr = -1
print('done', istr)

rawstr = input('Enter a number : ')
try:
    ival = int(rawstr)
except:
    ival = -1
if ival > 0:
    print('Nice work')
else :
    print('Not a number')