from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
from plotly import express as px
import csv


data_path='world-happiness-report-2021.csv'
happiness_data = pd.read_csv(data_path)
happiness = happiness_data.iloc[:, [0, 1, 2, 6, 7, 8, 9, 10, 11]]
#print(happiness)
happinessFilter = (happiness.loc[:, 'Ladder score'] >= 7.5)|\
                  (happiness.loc[:, 'Ladder score'] <= 3.5)
# sns.boxplot(x = 'Regional indicator', y = 'Ladder score', data = happiness, orient= 'v')
# plt.xticks(rotation =80)
# sns.barplot(x ='Ladder score', y ='Country name',
#               data =happiness[happinessFilter], palette ='coolwarm')
fig = px.sunburst(data_frame = happiness,
path = ['Regional indicator', 'Country name'],
values = 'Ladder score' ,
color = 'Ladder score')
fig = px.choropleth(data_frame = happiness,
locations = 'Country name',
locationmode = 'country names',
color = 'Ladder score')
fig.update_layout(title = '나라별 행복 지수', title_x = 0.5,
width = 900, height = 500)
fig.show
# fig = px.imshow(happiness.corr( ), text_auto = True) # 상관관계 실젯값 출력
# fig.update_layout(title = '상관관계 시각화', width = 800, title_x = 0.5)
# fig.show( )