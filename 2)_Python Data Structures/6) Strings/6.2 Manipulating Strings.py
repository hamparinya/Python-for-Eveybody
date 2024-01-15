#Concatenation Strings
a = 'Hello'
b = a + 'there'
print(b)            #-> Hellothere
c = a + ' ' + 'there'
print(c,'\n')       #

#Using in as a Logical Operator
x = 'banana'
'n' in x    #true
'm' in x    #false
'nan' in x  #True
if 'a' in x : #True
    print ("Found out\n")

#strings Comparation
if x == 'banana':
    print('All right, bananas.') #one conditions

y = input("Y = ")       
if y < 'banana' :    # A < a, Z < a
    print('Your word,' + y + ', comes before banana.\n')
elif  y > 'banana':
    print('Your word,' + y + ', comes after banana.\n')
else:
    print('All right, bananas.\n')

# String Library
greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print(greet)
print('Hi There'.lower())

print(type(greet),'\n')      #->    <class 'str'>
print(dir(greet))            
