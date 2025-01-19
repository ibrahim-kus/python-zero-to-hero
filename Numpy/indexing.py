import numpy as np

numbers = np.array([0,5,10,15,20,25,30,35,40])

print(numbers[0:3])
print(numbers[::]) # all
print(numbers[::-1]) #reverse 

numbers2 = np.array([[0,5,10],[15,20,25],[30,35,40]])
result2 = numbers2

print(numbers2)
print(numbers2[2])
print(numbers2[2][1])

####
array1 = np.arange(0,10)
array2 = array1 #referance

array2 = array1.copy() 

array2[0] = 20

print(array1)
print(array2)