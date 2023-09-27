
x = float(input("Enter the input X= "))
w = float(input("Enter the input W= "))

yin = x * w

if yin >= 0:
    y = 1
else:
    y = 0

print("Input(x)", x)
print("Weight(W)", w)
print("Net Input(yin) =", yin)

print("Output(y) ", y)
