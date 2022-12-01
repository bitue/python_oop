import csv 
from Airport import Airport
from math import sin, cos, sqrt, atan2, radians


class All_airport:
    def __init__(self) -> None:
        self.airports={}
        self.courency_rate={}
        self.country_code ={}
        self.load_data()

    def load_data(self):

        # country <--> BDT --- 0.788

        with open ('./data/rate.csv', 'r') as file :
            lines = csv.reader(file)
            for line in lines :
                self.courency_rate[line[1]] = line[2]
        file.close()

        # Bangladesh <---> BDT 

        with open ('./data/country_courancy_rate.csv', 'r') as file :
            lines = csv.reader(file)
            for line in lines :
                self.country_code[line[0]] = line[1]
        file.close()




        with open("./data/airport_info.csv", 'r', encoding="utf8") as file :
           lines =  csv.reader(file)
        #    print(lines)

           for line in lines:
                # print(line)
                get_country_name = line[3]
                get_code = self.country_code[get_country_name]
                rate = self.courency_rate[get_code]
                self.airports[line[4]] = Airport(line[4], line[1], line[2], line[3], line[6], line[7], rate)

           print(self.airports)
        file.close()
    
    def get_distance_calc(self, lat1, long1, lat2, long2):
        R = 6373.0

        lat1 = radians(lat1)
        lon1 = radians(long1)
        lat2 = radians(lat2)
        lon2 = radians(long2)

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c
        return distance
    
    def get_distance(self, air1_code, air2_code) :
        air1 = self.airports[air1_code]
        air2 =self.airports[air2_code]

        dis = self.get_distance_calc(air1.lat, air1.long, air2.lat, air2.long)

        return dis
    
    def price (self,start, end):
        dis = self.get_distance(start, end) 
        price = dis * self.airports[start].rate
        return price





   

all =  All_airport()

print(all.price("DAC", "PRA"))



           





