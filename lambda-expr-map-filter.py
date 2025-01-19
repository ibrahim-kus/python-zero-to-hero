
def square(num): return num ** 2

numbers = [1,3,5,7,9,12,4]

result = list(map(square,numbers))
print(result)

for item in map(square,numbers):
    print(item)
print("************lambda expression************************")
result2 = list(map(lambda num: num ** 2, numbers)) # lambda expression isimsiz bir fonksiyonla işimizi yapıyoruz map içerisinde aşağıdaki gibi isimde verebiliriz.
# square = lambda num: num ** 2
print(result2)

print("************filter************************")
#def check_even(num): return num%2==0
check_even = lambda num: num%2==0
#result3 = list(filter(check_even,numbers))
#result3 = list(filter(lambda num: num%2==0,numbers))
result3 = list(filter(check_even,numbers))
print(result3)