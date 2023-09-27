
w1 = 0
w2 = 0
b = 0
x1 = [1, 1, -1, -1]
x2 = [1, -1, 1, -1]
y = [1, -1, -1, -1]
print("Training Set: ")
print("x1: ",x1)
print("x2: ",x2)
print("Target(y): ",y)
for i in range(4):
 w1 = w1 + x1[i]*y[i]
 w2 = w2 + x2[i] * y[i]
 b = b + y[i]
 print("Training pair ",i+1)
 print("w1new: ", w1)
 print("w2new: ", w2)
 print("bnew: ", b)
print("Final weights: ")
print(w1)
print(w2)
print(b)