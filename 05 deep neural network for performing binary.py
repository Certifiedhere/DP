
from numpy import loadtxt
from keras.layers import Dense
from keras.models import Sequential
dataset = loadtxt("C:\\Users\\pima-indians-diabetes.csv", delimiter=',')


print(dataset)
X=dataset[:,0:8]
Y=dataset[:,8]
print(X)
print(Y)

model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam',
metrics=['accuracy'])
model.fit(X,Y,epochs=150, batch_size=10)

accuracy= model.evaluate(X,Y)
print("Accuracy of model is: ", (accuracy*100))

prediction=model.predict(X)
