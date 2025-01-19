import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3), index = ["A", "B", "C"], columns = ["Col1","Col2","Col3"])
print(df)
result = df 
print(result["Col1"])
print(type(result["Col1"])) # Series
result = df[["Col1","Col2"]]
print(result)
print("######1")
result = df.loc["A"] #location
print(result)
#loc["row","column"]  loc["row"] loc[":","colunm"]
print("######2")
result2 = df.loc[:,"Col1"]
result2 = df.loc[:,["Col1","Col2"]] # same as result = df[["Col1","Col2"]]
result2 = df.loc[:,"Col1":"Col3"] #interval
print(result2)
print("######3")
result3 = df.iloc[2] # index C
print(result3)
print("######4")
result4 = df.loc["C","Col1"]
result4 = df.loc[["A","B"],["Col1","Col2"]] #return dataframe
print(result4)
print("######5")
df["Col4"] = pd.Series(randn(3),["A","B","C"])
df["Col5"] = df["Col1"] + df["Col4"]

result5 = df.drop("Col5", axis=1) #col5 not remove from df
result5 = df.drop("Col5", axis=1,inplace = True) # col5 remove from df
print(df)
print(result5)