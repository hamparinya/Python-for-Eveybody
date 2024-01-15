#Constants 
print(123)            #Integer

print(98.6)           #Float

print('Hello world')  #String

#Python Varible Name Rules
# Good: spam    eggs    spam23  _speed
# Bad:  23spam  #sign   var.12
# Different:    spam    Spam    SPAM

# Sentence or Lines
x = 2 # <- Assignment statement
x = x + 2 #<-Assignmet with expresion
print(x)    #Print statement
'x is Viable' '= is Operator' 
'2 is Constant' 'print is Function'

#Operator Precedence
# Parenthesis > Power > Mutplication > Additon > Left to Right

# What does "Type" mean?
ddd = 1 + 4
print(ddd)      #->5
eee = 'hello '+ 'there'
print(eee)      #->hello there

#Type Matters
'''eee = eee + 1''' # It does not print out because they are difference type.
print(type(eee))
print(type('hello'))
print(type(1))

#Several Types of Numbers 
xx = 1
print(type(xx))     #->     <class 'int'>

temp = 98.6 
print(type(temp))   #->     <class 'float'>


#Type Conversations
print(float(99) + 100)
i = 42
print(type(i))
f = float (i)
print(type(f))     

# Integer Division
print(10 / 2)
print( 9 / 2)
print( 99 / 100)

# String Conversions
sval = '123'
print(type(sval))
#print(sval +1 )   # It is error
ival = int(sval)
print(type(ival))

print(ival + 1) # 123 + 1
nsv = 'hello bob'
try:
    niv = int(nsv)       # It is error


#User Input
except:
    nam = input('Who are you ? :')
print('Welcome ', nam)