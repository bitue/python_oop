import random

class Account:
    def __init__(self, ac_name, balance) -> None:
        self.ac_name = ac_name
        self.balance = balance
        self.__ac_id = 0 
        self._pro_id = 120 

    def _get_name(self):
        return self.ac_name
    def __set_ac_id(self):
        self.__ac_id = 200
    
    def set_ac_id (self, password):
        if(password == 100):
            self.__set_ac_id()
        else :
            print("Invalid pass")
    
    def get_ac_id(self, password):
        if(password == 100):
            return self.__ac_id 
        else :
            return "Invalid pass"


    
class Student_account (Account):
    def __init__(self, ac_name, balance, school) -> None:
        self.school = school 
        super().__init__(ac_name, balance)

st = Student_account("Ash", 1200, 'pzs')
print(dir(st))
    