#for
#while
x =1
while x < 100:
    print(x)
    x +=1
#range
for item in range(5,100,10): # Between 5 and 100, increasing by 10
    print(item)
for item in range(10): 
    print(item)
#
numbers = [x for x in range(10)]
print(numbers)
print("*****IS PRIME NUMBER****************************") # ASAL SAYI

number = int(input("Enter Number:"))
isPrime = True
if number == 1:
    print("1 not a prime")

for i in range (2,number):
    if (number % i == 0):
        isPrime = False
        break

if isPrime:
    print("is Prime")
else:
    print("is not Prime")

