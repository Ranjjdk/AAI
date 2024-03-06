import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
from sklearn.svm import SVC 
iris = load_iris() 
iris.feature_names 
iris.target_names 
df = pd.DataFrame(iris.data, columns=iris.feature_names)
print(df) 
df['target'] = iris.target 
df['flower_name'] = df.target.apply(lambda x : iris.target_names[x]) 
df0 = df[:50] 
df1 = df[50:100] 
df2 = df[100:150] 
plt.xlabel('Sepal Length') 
plt.ylabel('Sepal Width') 
plt.scatter(df0['sepal length (cm)'], df0['sepal width (cm)'], color='green', marker='+') 
plt.scatter(df1['sepal length (cm)'], df1['sepal width (cm)'], color='red', marker='.') 
X = df.drop(['target', 'flower_name'], axis='columns') 
y = df.target 
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2) 
model=SVC() 

model.fit(X_train, y_train) 
model.score(X_test, y_test)
