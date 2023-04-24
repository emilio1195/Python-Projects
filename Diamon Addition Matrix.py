import numpy as np
size = (3,3) #(row,column)
mP = np.random.randint(1,10,size)
print('Original Matrix\n', mP)
print("")
addition = 0
fila = size[0] - 1
for i in range(size[0]):
    mP[fila - i, i] = 0
    mP[i, i] = 0
print(mP)
for i in mP:
    for num in i:
        addition += num
print('The sum is: ', addition)