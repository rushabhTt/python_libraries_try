import numpy as np

# arr = np.array(42)                                                       # 0-D Arrays
# arr = np.array([1, 2, 3, 4, 5])                                          # 1-D Arrays
# arr = np.array([[1, 2, 3], [4, 5, 6]])                                   # 2-D Arrays
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])         # 3-D Arrays

# print(arr)

# print(type(arr))


# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)



# arr = np.array([1, 2, 3, 4])

# print(arr[2] + arr[3])



# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# print('2nd element on 1st row:', arr[0, 1])



# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# print('Last element from 2nd dim:', arr[1, -2])



# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[2:-1])



# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[1:5:2])



# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[1, 1:4])

# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[0:2, 2])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])