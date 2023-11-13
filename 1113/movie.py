import pandas as pd
from sklearn.ensemble import RandomForestRegressor

train = pd.read_csv('../data/movies_train.csv')
test = pd.read_csv('../data/movies_test.csv')

train.info()

# 결측치가 많은 데이터 제거
train = train.drop(['dir_prev_bfnum'],axis = 1)
test =  test.drop(['dir_prev_bfnum'],axis = 1)

# 제목 : 의미가 없기 때문에 제거
train = train.drop(['title'],axis= 1)
test = test.drop(['title'],axis= 1)

train.distributor.value_counts()

