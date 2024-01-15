fname = input('Enter the file name : ')
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
