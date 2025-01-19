
# file = open("newfile.txt","r",encoding="utf-8")

# content = file.read()
# print(content)

# file.close()



with open("newfile.txt","r",encoding="utf-8") as file: # not need close method
    content = file.read()
    print(content)
    file.seek(10) # go to cursor 10
    print(file.tell()) # current cursor location
    content2 = file.read()
    print(content2)
