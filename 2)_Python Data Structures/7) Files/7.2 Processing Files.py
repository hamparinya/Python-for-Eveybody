#Use for iterate thoght a sequence
xfile = open('mbox-short.txt')
for cheese in xfile: #if find out cheese, It will be printed
    print(cheese) 

#Counting Lines in a File
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line count', count)

#Reading the Whole things inp
fhand = open('mbox-short.txt') 
inp = fhand.read() #read() is read whole file
print(len(inp))
print(len(inp[:20]))

#Searching Through a File
fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:'):
        print(line)
# fixed Not need \n
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

#skipping with Continue
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)


#Using in to select lines
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)

fname = input('Enter the file name: ') #<- Prompt for File Name
fhand = open(fname)
count =0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject linew in', fname) #-> There were 27 subject linew in mbox-short.txt


#Bad file Names
fname = input('Enter the file name')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
count = 0 #try is true will  run this line
for line in fhand:
    if line.startswith('Subject'):
        count = count + 1
print('There were', count, 'subject linew in', fname)


