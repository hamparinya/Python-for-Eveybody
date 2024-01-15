x = input('Enter a number : ')
try:
    xi = int(x)
except:
    xi = -1
if xi >= 0:
    print('Nice work')
else:
    print('Not a number')
