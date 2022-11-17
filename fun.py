from abc import ABC , abstractmethod

class mo:
    def __init__(self) -> None:
        pass

class Computar(ABC, mo):
   
    def __init__(self) -> None:
        super().__init__()
        self.__name = ""
    

    @property 
    def set_property(self, name):
        self.__name = name 

    @abstractmethod
    def run(self):
        pass
    
    @abstractmethod
    def eat(self):
        pass
    

class Laptop(Computar):
    def run(self):
        print(".............")
    def eat(self):
        print('Eat that frog')
   


com = Laptop() 
print(com.eat())


