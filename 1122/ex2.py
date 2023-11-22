import numpy as np
x=np.array([2,4,6,8])
y=np.array([81,93,91,97])
mx = np.mean(x)
my=np.mean(y)
print(mx)
print(my)

divisor=sum([(i -mx)**2 for i in x])

def top(x,mx,y,my):
    d=0
    for i in range(len(x)):
        d += (x[i] -mx)*(y[i]-my)
    
    return d

dividend = top(x,mx,y,my)

print('분모',divisor)
print('분자',dividend)

# 기울기 a를 구하는 식
a= dividend/divisor

# y절편 b
b = my -(mx*a)

print(a,b)

fake_a = 3
fake_b = 76

def predict(x):
    return fake_a * x + fake_b

predict_result = []

for i in range(len(x)):
    predict_result.append(predict(x[i]))
    print("공부시간 = %.f, 실제점수 = %.f,  예측점수 = %.f"%(x[i],y[i],predict(x[i])))

n = len(x)
def mse(y, y_pred):
    return (1/n)* sum((y-y_pred)**2)

print("평균 제곱 오차 값",mse(y, predict_result))