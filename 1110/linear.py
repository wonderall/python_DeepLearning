import numpy as np

def linear_model(w0,w1,x):
    f_x= w0+w1 *x
    return f_x

def loss(f_x,y):
    ls = np.mean(np.square(y-f_x))
    return ls

def gradient_descent(w0,w1,x,y):
    gradient0 = 2 * np.mean((y-(w0+w1*x))*(-1))
    gradient1 = 2 * np.mean((y-(w0+w1*x))*(-1*x))
    return np.array([gradient0, gradient1])

def main():

    X = np.array([1,2,3,4]).reshape((-1,1))
    y = np.array([3.1, 4.9, 7.2, 8.9]).reshape((-1,1))

    # 파라미터 초기화
    w0 = 0
    w1 = 0

    # learning rate 설정
    lr = 0.001

    # 반복 횟수 1000으로 설정
    for i in range(1000):

        gd = gradient_descent(w0, w1, X, y)

        w0 = w0 - lr * gd[0]
        w1 = w1 - lr * gd[1]

        # 100회마다의 해당 loss와 w0, w1 출력
        if (i % 100 == 0):

            loss = loss(linear_model(w0,w1,X),y)

            print("{}번째 loss : {}".format(i, loss))
            print("{}번째 w0, w1 : {}, {}".format(i, w0, w1),'\n')

    return w0, w1