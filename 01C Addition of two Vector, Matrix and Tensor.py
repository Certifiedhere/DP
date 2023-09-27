import numpy as np
import tensorflow as tf


X = np.array([1, 2, 3, 4])
Y = np.array([5, 6, 7, 8])
Z = X + Y
print("Addition of two Matrix", Z)

A = np.array([[1, 2], [3, 4], [5, 6]])
B = np.array([[2, 5], [7, 4], [4, 3]])
C = A + B
print("Addition of two Vectors", C)

tensor_A = tf.constant([[4, 2]], dtype=tf.int32)
print("A:- ", tensor_A)
tensor_B = tf.constant([[7, 4]], dtype=tf.int32)
print("B:- ", tensor_B)
tensor_Addition = tf.add(tensor_A, tensor_B)

print("Addition tensor:- ", tensor_Addition)
