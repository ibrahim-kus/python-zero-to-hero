# return function from function 
def usAlma(number):
    
    def inner(power):
        return number ** power
    return inner # as function

two = usAlma(3)
print(two(4))

