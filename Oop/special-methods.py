
class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("Movie object was created")
    
    def __str__(self):
        return f"{self.title} by {self.director}"
    
    def __len__(self):
        return self.duration
    
    def __del__(self):
        print("Film was removed")

m1 = Movie('filmname','ibrahimm',130)

print(type(m1))
print(m1) #printed memory address before str method
print(str(m1)) #printed memory address efore str method

#del m1 # delete object kullanmasak bile bir süre sonra bellekten silinir.

# Please search in google python special methods.
