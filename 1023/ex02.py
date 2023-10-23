import numpy as np

num = np.array([[4],[5],[6]])
num2 = np.array([[1,2,3]])
num3 = np.array([[1,2,3],[4,5,6]])
num4 = np.array([[1,2],[3,4],[5,6]])
print(num2@num) # [[32]]
print(num3)
'''
[[1 2 3]
 [4 5 6]]
'''
print(num4)
'''
[[1 2]
 [3 4]
 [5 6]]
'''
print(num3@num4)
'''
[[22 28]
 [49 64]]
'''
print(np.sum(num4, axis=0)) #[ 9 12]
print(np.sum(num4, axis=1)) #[ 3  7 11]