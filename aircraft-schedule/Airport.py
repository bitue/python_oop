

class Airport :
    def __init__(self,code, name, city, country, lat, long, rate) -> None:
        self.code = code
        self.name =name 
        self.city =city
        self.country =country
        self.lat =float(lat)
        self.long =float(long)
        self.rate =float(rate)
    
    def __repr__(self) -> str:
        return f" airport code {self.code} name : {self.name} city {self.city} country {self.country}  rate ={self.rate}\n"