import csv
from Aircraft import Aircraft


class Airline :
    
    def __init__(self) -> None:
        csv_file = "./data/aircraft.csv"
        self.air_crafts ={}
        self.load_aircraft(csv_file)
        
       
        

    def load_aircraft(self, csv_file ):
        with open(csv_file, 'r') as file :
            lines = csv.reader(file)
            next(lines)
            for line in lines:
                
              self.air_crafts[line[0]] = Aircraft(line[3], line[0], line[1], line[4])
        file.close()


        for air in self.air_crafts :
            print(self.air_crafts[air])
                


Airline()
        
    