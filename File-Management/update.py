
# with open("newfile.txt","r+",encoding="utf-8") as file:
#     file.seek(20)
#     file.write("Deneme")

# with open("newfile.txt","r+",encoding="utf-8") as file: # r+ read and write
#     print(file.read())


with open("newfile.txt","a",encoding="utf-8") as file:  #append
    file.write("\nAppend İbrahim Kuş")


# ***** Sayfa ortasında güncelleme *****

with open("newfile.txt","r+", encoding="utf-8") as file:
    list = file.readlines()
    list.insert(1,"Yılmaz Aygün\n")
    file.seek(0)
    file.writelines(list)

with open("newfile.txt","r", encoding="utf-8") as file:
    print(file.read())
