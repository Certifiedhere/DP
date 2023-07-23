from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import MinMaxScaler
from sklearn.datasets import make_blobs
X, Y = make_blobs(n_samples=100, n_features=2, centers=2, random_state=1)
scalar = MinMaxScaler()
scalar.fit(X)
X = scalar.transform(X)
model = Sequential()
model.add(Dense(4, input_dim=2, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
print("Name:- Nihal Siddiqui, Roll NO. KFMSCCS024")
model.summary()
model.compile(loss='binary_crossentropy', optimizer='adam')
model.fit(X, Y, epochs=500)
Xnew, Yreal = make_blobs(n_samples=3, centers=2, n_features=2,
                         random_state=1)
Xnew = scalar.transform(Xnew)
Yclass = model.predict_step(Xnew)
Ynew = (model.predict(Xnew) > 0.5).astype("int32")
for i in range(len(Xnew)):
    print("X=%s, Predicted_probability=%s, Predicted Class=%s" % (Xnew[i],
                                                                  Ynew[i], Yclass[i]))
