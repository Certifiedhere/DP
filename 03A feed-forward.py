

x1 = float(input("Enter the input x1: "))
x2 = float(input("Enter the input x2: "))
w11 = float(input("Enter the input w11: "))
w12 = float(input("Enter the input w12: "))
w21 = float(input("Enter the input w21: "))
w22 = float(input("Enter the input w22: "))

yin1 = (x1*w11) + (x2*w21)
yin2 = (x1*w12) + (x2*w22)


if yin1 >= 0:
    y1 = 1
else:
    y1 = -1


if yin2 > 0:
    y2 = 1
else:
    y2 = -1

print("x1 ", x1)
print("x2 ", x2)
print("w11 ", w11)
print("w12", w12)
print("w21 ", w21)
print("w22 : ", w22)
print("yin1", yin1)
print("yin2", yin2)
print("y1 ", y1)
print("y2 ", y2)
