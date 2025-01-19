# Inheritance Kalıtım - Miras Alma **

# Person => name, lastname, age, eat(), drink()
#Student(Person), Teacher(Person)

class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print('Person instance created')

    def who_am_i(self):
        print('I am a person')
    
    def eat(self):
        print('I am eating')

class Student(Person): 
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname) #bunu yazmazsak person init ezilir ve yazılmaz.
        self.studentNumber = number
        print('Student instance created')
    #override (temel sunuftakini ezdi)
    def who_am_i(self):
        print('I am a Student')
    
    def eat(self):
        print('I am eating as Student')
    
    def sayHelloStudent(self):
        print('Hello I am a student')

class Teacher(Person):
    def __init__(self, fname, lname,branch):
        super().__init__(fname, lname) #alternative
        self.branch = branch
    
     #override (temel sunuftakini ezdi)
    def who_am_i(self):
        print(f'I am a {self.branch} Teacher')


p1 = Person('Ali', 'Yılmaz')
s1 = Student('veli', 'Turan',1245)
t1 = Teacher('Hasan', 'Yılmazoğlu', 'Math')

print(p1.firstName + ' '+ p1.lastName)
print(s1.firstName + ' '+ s1.lastName + ' ' + str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i()
s1.sayHelloStudent()
t1.who_am_i()


