import numpy as np

#result = np.array([1,3,5,7,9])
#result = np.arange(1,100,6)
#result = np.zeros(10)
result = np.ones(10)
result = np.linspace(0,100,5) # eşit aralıklarla 5 parçaya böler
print(result)

result2 = np.random.randint(0,10)
result2 = np.random.randint(1,10,3)
result2 = np.random.rand(4)
result2 = np.random.randn(4) #include negative
print(result2)

np_array = np.arange(50)
print(np_array)
np_multi = np_array.reshape(5,10) # 5 e 10 luk matris oluştur
print(np_multi)
print(np_multi.sum(axis=1)) #sum row 
print(np_multi.sum(axis=0)) #sum column

###
rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)
result4 = rnd_numbers.max()
print(result4)
result4 = rnd_numbers.argmax()
print(result4)