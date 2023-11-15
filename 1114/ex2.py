import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import tensorflow as tf
from keras import layers
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from matplotlib import pyplot as plt
from sklearn import tree


iris = datasets.load_iris()
X,Y= iris.data, iris.target
print(X,Y)
df = pd.DataFrame(X, columns=['꽃받침 길이','꽃받침 너비', '꽃이 길이', '꽃잎 너비'])
df['클래스'] = Y

train_x, test_x, train_y, test_y = train_test_split(X,Y, test_size=0.2, random_state=42)

print("원본 데이터 : \n", df.head(), '\n')
print('train_x:')
print(train_x[:5],'\n')
print('train_y:')
print(train_y[:5],'\n')

print('test_x:')
print(test_x[:5],'\n')
print('test_y:')
print(test_y[:5],'\n')

DTmodel = DecisionTreeClassifier()
DTmodel.fit(train_x, train_y)

# plt.rc('font', family ='NanumGothicEcoBold')
# fig =plt.figure(figsize =(25,20))
# _ = tree.plot_tree(DTmodel,
#                    feature_names=['꽃받침 길이','꽃받침 너비', '꽃잎 길이', '꽃잎 너비'],
#                    class_names=['setosa', 'versicolor', 'virginica'],
#                    filled=True)
# fig.savefig("decision_tree.png")

plt.rc('font', family='NanumBarunGothic')
fig = plt.figure(figsize=(25,20))
_ = tree.plot_tree(DTmodel,
                   feature_names=['꽃받침 길이','꽃받침 넓이', '꽃잎 길이', '꽃잎 넓이'],
                   class_names=['setosa', 'versicolor', 'virginica'],
                   filled=True)

fig.savefig("decision_tree.png")