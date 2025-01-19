
def my_decorator(func): # parameter is a function
    def wrapper():
        print("before from function execution")
        func() # referansı
        print("after from function execution")
    return wrapper

def sayHello():
    print("hello")

def sayGreeting():
    print("Greeting")

sayHello = my_decorator(sayHello)
sayHello()
print("************")####
sayGreeting = my_decorator(sayGreeting)
sayGreeting()

