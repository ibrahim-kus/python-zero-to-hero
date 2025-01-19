#String Formatting
name = "Hayrettin"
surname = "Hayal"
age = 37
print("my name is {}".format(name))
print("my name is {1} {0}".format(name,surname))

result = 200 / 700
print("result is {r:1.4}".format(r=result))

print(f"my name is {name} surname {surname} age {age}") # new 