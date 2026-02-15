import numpy as np

first_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(first_array.ndim)
print(first_array.shape)
print(first_array.size)
print(np.arange(10).reshape(2, 5).T)
print(np.zeros((3, 3)))
print(np.ones((2, 2)))
print(np.identity(4))
print(np.random.random(3))
print(np.random.randint(5, 20, 38))
print(first_array.min(axis=1))