import numpy as np
import tensorflow as tf

print("Name: Nihal Siddiqui, Roll No. KFMSCCS024")

A = np.array([[1, 2], [3, 4], [5, 6]])
print("A :- ", A)
B = np.array([[2, 5], [7, 4], [5, 6]])
print("B :- ", B)
C = A * B
print("Multiplication of two matrix: ", C)

X = np.array([1, 2, 3, 4])
Y = np.array([5, 6, 7, 8])
Z = X * Y
print("Multiplication of two matrix: ", Z)

tensor_A = tf.constant([[4, 2]], dtype=tf.int32)
print("A :- ", tensor_A)
tensor_B = tf.constant([[7, 4]], dtype=tf.int32)
print("B :- ", tensor_B)

tensor_multiply = tf.multiply(tensor_A, tensor_B)
print("tensor_multiply:- ", tensor_multiply)
