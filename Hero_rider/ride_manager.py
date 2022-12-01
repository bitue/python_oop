class Ride_manager :
    
    def __init__(self) -> None:
        self.available_cars = []
        self.available_bikes =[]
        self.available_cngs =[]

        

    def add_available_vehicle(self, vehicle_type, vehicle):
        if vehicle_type =='car':
            self.available_cars.append(vehicle)
        elif vehicle_type=='bike':
            self.available_bikes.append(vehicle)
        elif vehicle_type =='cng':
            self.available_cngs.append(vehicle)


uber = Ride_manager()