list = [2,4,6,7]

# for i in list: # list is iterable object... for döngüsü otomatik iteratörü oluşturur.
#     print(i)
#     print(dir(list)) # list methods
print("*****************Manuel Iteration**********************")

iterator = iter(list)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

print("*****************My Iterator as a List**********************")
class MyNumbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration

list = MyNumbers(20,50)

myiter = iter(list)

# print(next(myiter))
# print(next(myiter))

while True:
    try:
        element = next(myiter)
        print(element)
    except StopIteration:
        break
