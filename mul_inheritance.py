class Person :
    def __init__(self, name, dob, place) -> None:
        self.name=name
        self.dob=dob 
        self.place=place
    
    def walk(self):
        print(f'{self.name} is now walking .....')


class Student :
    def __init__(self, roll, id) -> None:
        self.roll = roll 
        self.id = id 


class Son(Student, Person) :
    def __init__(self, roll, id, name, dob, place ) -> None:
        Student.__init__(self, roll, id)
        Person.__init__(self, name, dob, place)




Bitue = Son(12, 33, "aa", "30-08-1998", "pabna")
print(Bitue.dob, Bitue.id)
    
  

        
        