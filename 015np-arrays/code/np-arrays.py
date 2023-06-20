import numpy as np

def arrays(arr):
    arr = np.array(arr, float)
    return arr[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)