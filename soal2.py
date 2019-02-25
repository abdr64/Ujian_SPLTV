import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

a = np.array([
    [1,-2,1],
    [3,1,-2],
    [7,-6,-1]
])
b = np.array([
    6,
    4,
    10
])
hasil = np.linalg.solve(a, b)

x = round(hasil[0])
y = round(hasil[1])
z = round(hasil[2])

print('Nilai x = ', x)
print('Nilai y = ', y)
print('Nilai z = ', z)