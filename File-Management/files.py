# #file = open("newfile.txt","w")
# #file = open("/home/ibo/Desktop/python-zero-to-hero/File-Management/newfile.txt","w",encoding="utf-8")
# file = open("newfile.txt","a",encoding="utf-8") # append mode
# print(file)
# 


# file.close()

file = open("newfile2.txt","x",encoding="utf-8") # create mode
print(file)
file.write("ibrahimxx11\n")
file.close()
