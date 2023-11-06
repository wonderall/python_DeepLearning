import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

student_data = pd.read_csv("../data/Student_Marks.csv")
print(student_data.info())
print(student_data.head())
print(student_data.describe())

student_corr = student_data.corr( ) # 상관관계(correlation) 분석
student_corr
sns.heatmap(student_corr, annot = True)
plt.show()