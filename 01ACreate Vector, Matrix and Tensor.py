import numpy as np
import tensorflow as tf

A = np.array([1, 2, 3, 4])
print("Create a vectors: ", A)

X = np.array([[1, 2], [3, 4], [5, 6]])
print("Create a vectors: ", X)

tensor_A = tf.constant([[1, 2]], dtype=tf.int32)

print("Create a tensor: ", tensor_A)
