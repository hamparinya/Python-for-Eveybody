#Finding the Average in a Loop
C = 0
S = 0
print('Before', C, S)
for x in [9, 41, 12, 3, 74, 15]:
    C = C + 1
    S = S + x
    print(C, S, x)
print('After', C, S, int(S/C))

#Filtering in a Loop
print('Before')
for x in [9, 41, 12, 3, 74, 15]:
    if x>20 :
        print ("Large number", x)
print("After")

#Search Using a Boolean Variable
found = False
print('Before', found)
for x in [9, 41, 12, 3, 74, 15]:
    if x == 3 :
        found = True
    print(found, x)  #ขยับ print ทำให้ loop หายไปได้
print("After", found)

#How to find the Smallest Value
Smallest = None
print('Before')
for x in [9, 41, 12, 3, 74, 15]:
    if Smallest is None :
        Smallest = x
    elif x < Smallest :
        Smallest = x
    print(Smallest, x)
print('After', Smallest)
