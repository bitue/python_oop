
class Student:
    def __init__(self, name , roll) -> None:
        self.name = name 
        self.roll = roll 
        self.__iq =100 
    
    @property
    def get_iq (self):
        return self.__iq
    
    @get_iq.setter
    def set_iq(self, roll):
        self.__iq = self.__iq + 100 
    

        
    

    



me = Student("ash", 12)

me.set_iq
print(me.get_iq)

        