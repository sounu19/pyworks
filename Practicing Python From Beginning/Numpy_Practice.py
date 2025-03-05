import numpy as np
from numpy import random

'''arr = np.array([1,2,3,4,5,6,7])

filter_arr = []

for element in arr:
    if element % 2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr = arr [filter_arr]

print(arr)
print(filter_arr)
print(newarr)'''

'''arr = np.array([41,42,43,44])

filter_arr = arr > 42
new_arr = arr[filter_arr]
print(new_arr)'''

x = random.binomial(n=10, p=0.5, size=10)

print(x)
