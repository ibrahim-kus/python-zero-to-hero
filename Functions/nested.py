

#encapsulation
def outer(num1):
    print("Outer f.")
    def inner_increment(num1):
        print("İnner f.")
        return num1 + 1
    
    num2 = inner_increment(10)
    print(num1,num2)
    

print(outer)
outer(10)

######

def factorial(number):
    if not isinstance(number, int):
        raise TypeError("number must be an integer")

    if not number >=0:
        raise ValueError("number must be zero or positive")

    def inner_factorial(number):
        if number <= 1:
            return 1

        return number * inner_factorial(number - 1)

    return inner_factorial(number)
try:
    print(factorial(4))
except Exception as ex:
    print(ex)