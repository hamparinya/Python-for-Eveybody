#Repeated steps
n = 5
while n > 0 : #From true become false
    print(n)
    n = n - 1 #repeat until 0
print ('Blastoff')
print(n)

# An Infinitee Loop
n = 0
while n > 0 :
    print('Lather')
    print('Rinse')  #It will loop infinite, If n > 0
print('Day off!')   #It will do not show, If n > 0

#Breaking Out of a Loop
while True:
    line = input('> ')
    if line == 'done':
        break   # stop loop
    print(line)
print('Done!')

#Finishing an Iteration with continue
while True :
    line = input('Write something : ')
    if line[0] == '#':
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')
