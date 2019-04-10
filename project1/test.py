import numpy as np


array = np.arange(0, 20, 1)
array = array.reshape([4, -1])

bb = array[[1,3,6]]
print(bb)

print('number of dim:', array.ndim)
print('shape:', array.shape)
print('size:', array.size)
print(array)
print(array[:, 2])
print(array[..., 2])
print(array[:array.shape[1], 2:])
