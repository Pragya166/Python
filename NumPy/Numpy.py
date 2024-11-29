import sys
# print(sys.version)
# print(sys.executable)

import numpy as np 
# array=np.array([1,"Hello",True,4,5])
# print(array)
# print(np.__version__)
# print(np.array((1,2,3)))
# print(np.array((4)))
# print(np.array([[1,2,3],[4,5,6]]))
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(arr)



a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

# arr = np.array([1, 2, 3, 4], ndmin=5)

# print(arr)
# print('number of dimensions :', arr.ndim)
print(b[0])
print(c[1,2])
print(d[1,1,2])

