#Assignment 5.2
'''5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
Once 'done' is entered, print out the largest and smallest of the numbers. 
If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
Enter the numbers 7, 2, bob, 10, 4 and Match the desired output as shown.'''
x = 0
large = -1
small = None
while True:
    x = input('Enter a number : ')
    if x == 'done' or x == 'Done':
        break
    try:
        xi = int(x)
    except:
        print('Invalid input')
        continue
    if small is None:
        small = xi
    elif xi < small:
        small = xi
    elif xi > large:
         large = xi
print('Max number is ', large)
print('Min Number is ', small)


