import numpy as np
import tensorflow as tf
print("Name: Nihal Siddiqui, Roll No. KFMSCCS024")

X = np.array([1, 2, 3, 7, 3, 5, 2])
Y = np.array([[1], [2], [3], [5], [7], [8], [8], [2]])
Z = X * Y
print("Multiply matrix with vector", Z)

W = [2, -3]
U = [1, 3]
dotproduct = np.dot(U, W)
print("Matrix of Dot Product", dotproduct)

A = np.array([[6, 1, 1, ], [4, -2, 5], [2, 8, 7]])
print("Inverse of the matrix: ", np.linalg.inv(A))
