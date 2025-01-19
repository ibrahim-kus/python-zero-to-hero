# method
list = [1,2,3,4,5]
list.append(8) # method
list.pop() #method
print(list)
#print(help(list.append))

#function
def hello():
    print("Hello")

hello()
print("************Function Examples**************")
#*args , **args 
def add(*params):
    print(type(params))
    print(params) # as tuple
    return sum((params))

print(add(10,20,30,40))

def displayUser(**args): #belirsiz elemanlı dictionary gelecek 
    print(type(args))
    for key,value in args.items():
        print('{} is {}'.format(key,value))

displayUser(name="ibo", age=55)
displayUser(name="iboxxx", age=59,city="antalya")
