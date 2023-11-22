import matplotlib.pyplot as plt
from tensorflow import sequence
from tensorflow import sequence

model = Sequential()
model.add(Dense(1, input_dim=1, activation='sigmoid'))

# 교차 엔트로피 오차 함수를 이용하기 위하여 'binary_crossentropy'로 설정합니다.
model.compile(optimizer='sgd' ,loss='binary_crossentropy')
model.fit(x, y, epochs=5000)
model = Sequential()
model.add(Dense(1, input_dim=1, activation='sigmoid'))

# 교차 엔트로피 오차 함수를 이용하기 위하여 'binary_crossentropy'로 설정합니다.
model.compile(optimizer='sgd' ,loss='binary_crossentropy')
model.fit(x, y, epochs=5000)


plt.scatter(x,y)
plt.plot(x, model.predict(x), 'r')
plt.show()

hour = 7
prediction = model.predict([hour])
print("%.f 시간을 공부할 경우, 합격 예상 확률은 %.01f%% 입니다." %(hour, prediction *100))