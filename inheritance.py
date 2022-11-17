class Person :
    def __init__(self, name, dob, place) -> None:
        self.name=name
        self.dob=dob 
        self.place=place
    
    def walk(self):
        print(f'{self.name} is now walking .....')


class Son(Person):
    def __init__(self, name, dob, place, father , mother) -> None:
        super().__init__(name, dob, place)
        self.father = father
        self.mother = mother
    
    def declare(self):
        print("He is my son....")
    
   
    

class Student(Son):
    def __init__(self, name, dob, place, father, mother, roll) -> None:
        super().__init__(name, dob, place, father, mother)
        self.roll = roll 
    
    def study(self):
        print(f"{self.name} is reading ... ")


bitue = Student("bitue", "30-08-1998", "pabna", "shaheen", "beauty", 13)
print(bitue)
    


        