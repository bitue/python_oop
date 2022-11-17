import time

class School:
    def __init__(self, name , reg, head, since) -> None:
        self.name =name
        self.res = reg 
        self.head = head 
        self.since = since
        self.teachers =[]
    
    def __repr__(self) -> None:
        return f'{self.name} is since at reppr {self.since}'
    
    # def __str__(self):
    #     return f'{self.name} is since at {self.since}'
    
    def boom(self):
        print("Deleting ...............", self.name)
        del self.name 
        
    


sc = School("PZS", "1909", "Lutfor", 1999)
sch = School("PS", "1909", "Lutfor", 1999)
print(sc)

