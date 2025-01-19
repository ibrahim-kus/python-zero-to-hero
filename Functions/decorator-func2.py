
# def my_decorator(func): # parameter is a function
#     def wrapper(name):
#         print("before from function execution")
#         func(name) # referansı
#         print("after from function execution")
#     return wrapper


# @my_decorator 
# def sayHello(name):
#     print("hello", name)

# sayHello("ibo")
######################################33
import math
import time

def calculate_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print("function"+func.__name__+ str(finish - start) + "second")
    return inner

@calculate_time
def usAlma(a,b):
    #start = time.time()
    #time.sleep(1)
    print(math.pow(a,b))
    #finish = time.time()
    #print("function" + str(finish - start) + "second")

@calculate_time
def factorial(num):
    #start = time.time()
    #time.sleep(1)
    print(math.factorial(num))
    #finish = time.time()
    #print("function" + str(finish - start) + "second")

usAlma(2,8)
factorial(60)