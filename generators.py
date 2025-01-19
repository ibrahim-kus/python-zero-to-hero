# bellekte yer işgal etmeyen iterator

# def cube():
#     result = []

#     for i in range(5000):
#         result.append(i**3)
#     return result

# print(cube())

def cube():
    for i in range(5):
        yield i ** 3 # produce and use. Not kept in memory


for i in cube():
    print(i)

print("#############")
print("#############")

list = [i**3 for i in range(5)]
print(list)
print("######result as generator #######")
generator = (i**3 for i in range(5))
print(generator)
# print(next(generator))
# print(next(generator))
# print(next(generator))
for i in generator:
    print(i)

