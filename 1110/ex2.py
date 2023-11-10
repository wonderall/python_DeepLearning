import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

data = {
    'X1': [8.70153760, 3.90825773, 1.89362433, 3.28730045, 7.39333004, 2.98984649, 2.25757240, 9.84450732, 9.94589513, 5.48321616],
    'X2': [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0],
    'Y': [5.64413093, 3.75876583, 3.87233310, 4.40990425, 6.43845020, 4.02827829, 2.26105955, 7.15768995, 6.29097441, 5.19692852]
}


df = pd.DataFrame(data)

# 독립 변수와 종속 변수 분리
X = df[['X1', 'X2']]
Y = df['Y']

# 모델 초기화 및 학습
lrmodel = LinearRegression()
lrmodel.fit(X, Y)

# 예측 결과 계산
Y_pred = lrmodel.predict(X)

# 회귀선 시각화
plt.scatter(X['X1'], Y, label='True Y') #그래프에 라벨(범례)을 설정 'True Y'는 이 산포도가 실제 데이터(종속 변수)를 나타낸다는 라벨입니다.
plt.plot(X['X1'], Y_pred, c='r', label='Predicted Y') #그래프에 라벨(범례)을 설정합니다. 'Predicted Y'는 이 그래프가 모델로부터 예측된 값(생존율 등)을 나타낸다는 라벨입니
plt.xlabel('X1')
plt.ylabel('Y')
plt.legend()
plt.show()