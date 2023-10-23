import numpy as np
num = np.array([[1,2,3],[4,5,6]])
print(np.mean(num))#3.5
print(np.mean(num, axis=0))#[2.5 3.5 4.5]
print(np.mean(num, axis=1))#[2. 5.]

num2 = np.array([[1,4,3,7,8],[1,2,5,7,3],[3,1,3,7,7]])
print(np.median(num2))#3.0
print(np.median(num2, axis=0))#[1. 2. 3. 7. 7.]
print(np.median(num2, axis=1))#[4. 3. 3.]

print(np.max(num2)) # 8 
print(np.min(num2)) # 1

print(np.min(num2, axis=0))# [1 1 3 7 3]  열 중에 작은값
print(np.min(num2, axis=1))# [1 1 1] 행 중에 작은값

print(np.max(num2, axis=0))# [3 4 5 7 8] 열 중에 큰값
print(np.max(num2, axis=1))# [8 7 7] 행 중에 큰값

print("위치 확인 함수 argmin, argmax")
print(np.argmin(num)) # 인덱스 값, 0
print(np.argmax(num2)) # 인덱스 값, 4