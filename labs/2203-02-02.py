import numpy as np
import matplotlib.pyplot as plt

matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 10]])

# see information about the matrix
print(f'Shape: {matrix.shape}')
print(f'size: {matrix.size}')
print(f'ndim: {matrix.ndim}')

# Dot operation with vectors
vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])
result = np.dot(vector_a, vector_b)
print(result)

matrix_a = np.array([[1, 1, 1],
                     [1, 1, 1],
                     [1, 1, 2]])

matrix_b = np.array([[1, 3, 1],
                     [1, 3, 1],
                     [1, 3, 8]])

result_add = np.add(matrix_a, matrix_b)
print(result_add)
result_subtract = np.subtract(matrix_a, matrix_b)
print(result_subtract)

matrix_c = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

print(matrix_c + 100)

# lambda function
add_100 = lambda i: i + 100
vectorized_add_100 = np.vectorize(add_100)
print(vectorized_add_100(matrix_c))


# print out max and minimum
matrix_d = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

print(f'max: {np.max(matrix_d)}')
print(f'min: {np.min(matrix_d)}')

# get min for columns
print(f'get min for columns: {np.min(matrix_d, axis=0)}')

# get min for rows
print(f'get min for rows: {np.min(matrix_d, axis=1)}')

print(f'mean : {np.mean(matrix_d)}')
print(f'var : {np.var(matrix_d)}')

print(f'mean column: {np.mean(matrix_d, axis=0)}')
print(f'var rows : {np.var(matrix_d, axis=1)}')

# Random nums
random_numbers = np.random.randint(0, 11, 3)
print(random_numbers)

random_normal = np.random.normal(0.0,1.0,3)
print(random_normal)

random_normal = np.random.normal(10.0,20.0,5000)
plt.plot(random_normal)