import pandas as pd
import numpy as np
#data 
numbers = [20,30,40,50]
letters = ['a','b','c','d']
mix = ['a','b','c',20]
dict = {'a':100, 'b':200, 'c':300, 'd':400}
random_numbers = np.random.randint(10,100,6)

#pandas_series = pd.Series()
pandas_series = pd.Series(numbers)
pandas_series2 = pd.Series(letters)
pandas_series3 = pd.Series(mix)
pandas_series4 = pd.Series(5,[0,1,2,3,4])
pandas_series5 = pd.Series(numbers, ['a','b','c','d']) # assign index 
pandas_series6 = pd.Series(dict)
pandas_series7 = pd.Series(random_numbers)

print(pandas_series)
print(pandas_series2)
print(pandas_series3)
print(pandas_series4)
print(pandas_series5)
print(pandas_series6)
print(pandas_series7)
print("########")
pandas_series8 = pd.Series([15,25,35],['a','b','c']) #assign index. 
print(pandas_series8[0]) # Değiştirsek bile sıfırıncı değeri 15 olarak verir.
print(pandas_series8['a']) # 15
print(pandas_series8.ndim) # Liste boyutu
print(pandas_series8.dtype)
print(pandas_series8.shape)
print(pandas_series8.sum()+ "----"+pandas_series8.max())