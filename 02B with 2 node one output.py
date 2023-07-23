import math
print("Name:- Nihal Siddiqui, Roll NO. KFMSCCS024")

x1 = float(input("Enter the input x1: "))
x2 = float(input("Enter the input x2: "))
w1 = float(input("Enter the input w1: "))
w2 = float(input("Enter the input w2: "))

bias = float(input("Enter bias: "))
yin = (x1*w1) + (x2*w2) + bias
ybin = 1/(1 + math.exp(-yin))
ybipolar = (2/(1 + math.exp(-yin))) + 1
print("Input X1", x1)
print("Input X2", x2)
print("Weight W1 = ", w1)
print("Weight W2 = ", w2)
print("Bias = ", bias)
print("Net Input Yin:", yin)
