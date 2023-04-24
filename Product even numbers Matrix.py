import numpy as np
size = (3,5) #(row,column)
mP = np.random.randint(1,20,size)
print('Original Matrix\n', mP)
print("")
for row in range(size[0]):
    product = 1
    for col in range(size[1]):
        elemento = mP[row, col]
        if elemento % 2 == 0:
            #even number
            product *= elemento
    if product == 1:
        product = 0
    print('Product of the even items, Row {i}: {prod}'.format(i=row, prod=product))