import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

name = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width',
'Class']
dataset = pd.read_csv("C:\\Users\\iris_csv.csv",
names=name)

print(dataset.head())


X=dataset.drop(['Class'],axis="columns")
Y=dataset['Class']

x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,
random_state=0)
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)


print("dataset before PCA")
print(x_train)
print(x_test)

pca = PCA()
x_train = pca.fit_transform(x_train)
x_test = pca.transform(x_test)

pca = PCA(n_components=2)
x_train = pca.fit_transform(x_train)
x_test = pca.transform(x_test)
print("\ndataset After PCA")

