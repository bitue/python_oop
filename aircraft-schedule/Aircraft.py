import csv 

class Aircraft :
    def __init__(self, make, code, type, flight_range ) -> None:
        self.make =make 
        self.code =code
        self.type =type
        self.flight_range = flight_range
    
    def get_name (self):
        return self.make
    
    def __repr__(self) -> str:
        return f"aircraft : {self.make} : code {self.code} type : {self.type}"
    # @staticmethod
    # def  reader ():
    #     with open("./data/aircraft.csv", "r") as file :
    #         lines = csv.reader(file)
    #         for line in lines:
    #             print(line)
    


