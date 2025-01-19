import numpy as np

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

print(numbers1)
print(numbers2)

result = numbers1 + numbers2    
print(result)

result = numbers1 +10
print(result)

#####
result = np.sin(numbers1) #sinus
print(result)
result = np.sqrt(numbers1) #sinus
print(result)
result = np.log(numbers1) #sinus
print(result)
####
multi_numbers1 = numbers1.reshape(2,3)
multi_numbers2 = numbers2.reshape(2,3)

print(multi_numbers1)
print(multi_numbers2)

result2 = np.vstack((multi_numbers1,multi_numbers2)) #vertical
result2 = np.hstack((multi_numbers1,multi_numbers2)) #horizontal
print(result2)

result = numbers1 >=50
print(result)