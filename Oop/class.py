
class Person:
    #pass # yer tutucu
    #class attributes
    address = "no information"
    #constructor(yapıcı metod)
    def __init__(self,name,year): # self mean that p1 or p2 object.
    #object attributes
        self.name = name
        self.year = year
        print('init metodu çalıştı')


    #methods
    #instance method 
    def intro(self): # self oluşturulan instance ı ifade eder. 
        print("Hello There " + self.name)
    
    #instance method
    def calculateAge(self):
        from datetime import datetime
        return datetime.now().year - self.year  

p1 = Person('ali',1980) #object(instance)
p2 = Person(name='veli',year=2000) #object(instance)

#print(p1)
#print(type(p1))
print(f'name : {p1.name} year: {p1.year} address : {p1.address}')
print(f'name : {p2.name} year: {p2.year} address : {p2.address}')

p1.intro()
print(f' Age : {p2.calculateAge()}')