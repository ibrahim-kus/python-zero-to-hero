class Circle:
    # Class object attribute
    pi = 3.14

    def __init__(self,yaricap=1): # yaricap belirtilmediyse 1 değeri ata
        self.yaricap = yaricap


    #Method
    def cevre_hesapla(self):
        return 2*self.pi*self.yaricap
    
    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)
    

c1 = Circle() # yaricap 1
c2 = Circle(5)

print(f'c1 alan: {c1.alan_hesapla()} çevre {c1.cevre_hesapla()} ')
print(f'c2 alan: {c2.alan_hesapla()} çevre {c2.cevre_hesapla()} ')