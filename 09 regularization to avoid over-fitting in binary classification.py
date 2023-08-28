import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
print("Name:- Nihal Siddiqui, Roll NO. KFMSCCS024")
#reading dataset
#url = "https:archive.ics.uci.edu/ml/machine-learningdatasets/iris/iris.data"
name = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width',
'Class']
dataset = pd.read_csv("C:\\Users\Admin\Desktop\KFMSCCS024\iris.data",
names=name)
#displaying dataset
print(dataset.head())
# X=dataset.drop('Class',1)
X=dataset.drop(['Class'],axis="columns")
Y=dataset['Class']
#splitting train and test data set
x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,
random_state=0)
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
#display train and test data set
print("dataset before PCA")
print(x_train)
print(x_test)
#Creating PCA object
pca = PCA()
x_train = pca.fit_transform(x_train)
x_test = pca.transform(x_test)
#giving a principal component 2
pca = PCA(n_components=2)
x_train = pca.fit_transform(x_train)
x_test = pca.transform(x_test)
print("\ndataset After PCA")