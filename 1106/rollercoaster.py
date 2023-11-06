import pandas as pd
import matplotlib.pyplot as plt


# df = pd.read_csv("../data/rollercoasters_bak.csv")
# print(df.shape)
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe())


# df2 = df.sort_values(by="max_speed", ascending = False)
# pd.set_option("display.max_columns",None)
# print(df2.iloc[0:10,[1,2,3]])

# x1 = df['rollercoaster_type'].unique()
# print(x1)

# x2 = df['rollercoaster_type'].nunique( )
# print(x2)

# rollercoaster_type_count = df['rollercoaster_type'].value_counts( )
# print(rollercoaster_type_count)

# plt.figure(figsize = (10,6))
# rollercoaster_type_count.plot.bar(width=0.9)
# plt.xlabel('rollercoaster_type')
# plt.ylabel('count')
# plt.text(0, 22.5, 22)
# plt.text(5, 7.5, 7)
# plt.text(13, 4.5, 4)
# plt.show()

# rollercoaster_type_count = df['rollercoaster_type'].value_counts()
# plt.figure(figsize=(10,6))
# rollercoaster_type_count.plot.bar(width = 0.9)
# plt.xlabel('rollercoaster_type')
# plt.ylabel('count')
# for i in range(len(x1)):
#   plt.text(i, rollercoaster_type_count[i]+0.5,
#            rollercoaster_type_count[i], va ='center',ha='center')
# plt.show()

df = pd.read_csv("../data/rollercoasters.csv")
corr=df.corr()
corr2 = corr['excitement']
corr3=corr2.sort_values(ascending=False)
corr3
corr3.plot.bar()
for i in range(len(corr3)):
  plt.text(i, corr3.iloc[i]+0.05, '%.2f' %corr3.iloc[i], va='center', ha='center')
plt.show()



