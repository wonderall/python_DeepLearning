import seaborn as sns
df = sns.load_dataset('../data/diamonds')
print(df.head())
print(sns.get_dataset_names())

df.info()
print(df.describe())