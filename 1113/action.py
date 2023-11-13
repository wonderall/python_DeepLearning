import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
movies = pd.read_csv('../data/movies_train.csv')
print("moveis -- ", movies)
data = movies.fillna(movies.median())
data.info()
plt.rc('font', family='NanumBarunGothic')
sns.pairplot(data, hue='genre', palette='RdBu', corner = True )

x = pd.get_dummies(X, columns =['distributor', 'genre', 'screening_rat'])
print(x)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test =train_test_split(x,y,test_size = 0.2, random_state=42)

cm_display=metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix)

cm_display.plot()
plt.title('Confusion Matrix')
plt.xlabel('predixted')
plt.ylabel('actual')
plt.show()