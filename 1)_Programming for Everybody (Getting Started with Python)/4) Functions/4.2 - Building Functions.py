#Building our Own Functions
x = 5
print('Hello')
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
print('Yo')
print_lyrics()
x = x + 2
print(x)


#Paremeters
def greet(lang) :
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else :
        print('Hello')
greet('en')
greet('es')
greet('fr')

#Return Values
def greet() :
    return "Hello"
print(greet(), "Glenn")
print(greet(), "Sally")

def greet(lang) :
    if lang == 'es':
        return 'Hola' #return is end function, If it have a Str will be print out
    elif lang == 'fr':
        return 'Bonjour'
    else :
        return 'Hello'   # if Not have a return, None will be printed out too
print(greet('en'),"Glenn")
print(greet('es'),"Sally")
print(greet('fr'),"Micheal")

#Multiple Parameters/Arguments
def addtwo(a, b):
    added = a + b
    return added
x = addtwo(3, 5)
print(x)

