print("Name:- Nihal Siddiqui, Roll NO. KFMSCCS024")
x1 = [1, 1, -1, -1]
x2 = [1, -1, 1, -1]
y = [1, 1, 1, -1]
print("Trainin Set: ")
print("x1: ", x1)
print("x2: ", x2)
print("Target(y): ", y)
print("Initializing the weights, bias and learing rate: ")
w1 = 0.1
w2 = 0.1
b = 0.1
a = 0.1
print("w1: ", w1, "\tw2", w2, "\tb: ", b, "\talpha: ", a)
print("x1\tx2\t\tyin\t\ty\t\tw1new\t\tw2new\t\tbnew")
print("-----------------------------------------")
for i in range(4):
    yin = b + ((x1[i]*w1) + (x2[i]*w2))*a
    dw1 = a * (y[i] - yin) * x1[i]
    dw2 = a * (y[i] - yin) * x2[i]
    db = (y[i] - yin)
    w1 = w1 + dw1
    w2 = w2 + dw2
    b = b + db

print(x1[i], "\t", x2[i], "\t\t", round(yin, 2), "\t\t", round(y[i], 2),
      "\t\t", round(w1, 2), "\t\t", round(w2, 2), "\t\t", round(b, 2))
