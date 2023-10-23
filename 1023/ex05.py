import numpy as np

sul = 2
rep_cnt = 5
result = np.repeat(sul, rep_cnt)
print(result)#[2 2 2 2 2]
print(type(result))#<class 'numpy.ndarray'>

array1 = np.array([11,2])
array2 = np.array([3,4])
result = np.concatenate((array1,array2))
print(result)#[11  2  3  4]

my_list = [10,"hello", True]
print(my_list[0])

my_list2 =[[1,2,3],[49,33,22]]
print(my_list2[1][1])

print(np.__version__)

arr1= np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])

con1 = np.concatenate((arr1,arr2))
print(con1)