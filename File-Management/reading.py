
file = open("newfile.txt","r",encoding="utf-8")
print(file)

for i in file:
    print(i,end="")

file.close()
print("************read() function")
filex = open("newfile.txt","r",encoding="utf-8")
content = filex.read(5)
content = filex.read(3)
print(content)
filex.close()