#Largest Value
Lar = -1
print('Before', Lar)
for num in [9, 41, 12, 3, 74, 15]:
    if num > Lar :
        Lar = num
    print(Lar, num)
print('After', Lar)

#Counting in a loop
zero = 0
print('before', zero)
for thing in [9, 41, 12, 3, 74, 15]:
    zero = zero + 1
    print(zero, thing)
print('After', zero)

#Summing in a loop
zero = 0
print('before', zero)
for thing in [9, 41, 12, 3, 74, 15]:
    zero = zero + thing
    print(zero, thing)
print('After', zero)
