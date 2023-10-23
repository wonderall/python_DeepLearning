import numpy as np

values = np.array([[1,3,4,5,6,1],[4,3,25,34,3,3]])

print(np.var(values))#표준편차
print(np.std(values))#분산

a = np.array([-1,3,2,-6])
b = np.array([3,6,12,2])
print(a)
print(b)

# 행렬 구성 바꾸기
a1 = np.reshape(a, [2,2])
print(a1)

b1 = np.reshape(b,[4,1])
print(b1)