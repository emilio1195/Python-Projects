import numpy as np
size = (3,3)
mP = np.random.randint(1,20,size)
print('Original Matrix\n', mP)
print("")

# diagonal
mD = np.zeros(size)
for i in range(size[0]):
    mD[i][i] = mP[i][i]
print('Diagonal Matrix\n', mD)

# upper diagonal
mDS = mP.copy()
for i in range(1, size[0]):
    for j in range(size[0]):
        if i != j & j < i:
            mDS[i][j] = 0
print('Upper Diagonal Matrix\n', mDS)

# lower diagonal
mDI = mP.copy()
for i in range(size[0]):
    for j in range(1, size[0]):
        if i != j & j > i:
            mDI[i][j] = 0
print('Lower Diagonal Matrix\n', mDI)
