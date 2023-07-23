
from numpy import loadtxt
from keras.layers import Dense
from keras.models import Sequential
dataset = loadtxt("given\diabetes.csv", delimiter=',')
print("Name:- Nihal Siddiqui, Roll NO. KFMSCCS024")
import numpy as np
from keras.layers import Dense
from keras.models import Sequential
model = Sequential()
model.add(Dense(units=2, activation='relu', input_dim=2))
model.add(Dense(units=1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam',
metrics=['accuracy'])
print(model.summary())
print( model.get_weights())
X = np.array([[0.,0.], [0.,1.], [1.,0.], [1.,1.]])
Y = np.array([0.,1.,1.,0.])
model.fit(X,Y, epochs=1000, batch_size=4)
print(model.get_weights())
print(model.predict(X, batch_size=4))

print(dataset)
X=dataset[:,0:8]
Y=dataset[:,8]
print(X)
print(Y)
#creating model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
#compiling model and fitting model
model.compile(loss='binary_crossentropy', optimizer='adam',
metrics=['accuracy'])
model.fit(X,Y,epochs=150, batch_size=10)
#Evaluating accuracy
accuracy= model.evaluate(X,Y)
print("Accuracy of model is: ", (accuracy*100))
#prediction
prediction=model.predict(X)