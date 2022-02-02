from unicodedata import name


class Person:
    #method is a function within a class 
    def __init__(self, full_name=""):  
        #__int__ = constructor | (self) = Every first mehtod inside of the class starts with this. (good convention) 
        self.full_name = full_name 

adam = Person("Adam Hayes") 
#this creates an instance of the "Person" class called "adam". Then passes "adam hayes" as full_name
print(adam.full_name)

eve = Person("Eve Chambers ") 
#this creates an instance of the "Person" class called "eve".
print(eve.full_name)

abel = Person("Abel Flanel")
print(abel.full_name)

#if __name__ == "__main__":
#    main()

#opopopopoopopopoopopopopopopopopoopopopopopopopopopopopo

class Restraunt:
    def __init__(self,name,cuisine,price,rating):
        self.name = name
        self.cuisine = cuisine
        self.price = price
        self.rating = rating
    
    def __str__(self):
        return self.name
