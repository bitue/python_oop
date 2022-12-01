from abc import ABC , abstractmethod

class Vehicle(ABC):
    speed_meter ={
        'car':50,
        'bike':25,
        'cng':20
    }
    def __init__(self, vehicle_type ,license_plate,  rate, driver ) -> None:
        self.vehicle_type = vehicle_type
        self.license_plate =license_plate
        self.rate =rate 
        self.driver = driver
        self.speed = Vehicle.speed_meter[self.vehicle_type]
        self.available ='available'
    
    @abstractmethod
    def start_driving(self):
        pass 
    @abstractmethod
    def end_trip(self):
        pass

class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver) -> None:
        super().__init__(vehicle_type, license_plate, rate, driver)
    
    def start_driving(self):
        print(f'{self.vehicle_type}  {self.license_plate} started')
        self.available ='unavailable'
        return super().start_driving()
    def end_trip(self):
        print(f'{self.vehicle_type}  {self.license_plate} ended ')
        self.available ='available'
        return super().end_trip()



class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver) -> None:
        super().__init__(vehicle_type, license_plate, rate, driver)
    
    def start_driving(self):
        print(f'{self.vehicle_type}  {self.license_plate} started')
        self.available ='unavailable'
        return super().start_driving()
    def end_trip(self):
        print(f'{self.vehicle_type}  {self.license_plate} ended ')
        self.available ='available'
        return super().end_trip()


class Cng(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver) -> None:
        super().__init__(vehicle_type, license_plate, rate, driver)
    
    def start_driving(self):
        print(f'{self.vehicle_type}  {self.license_plate} started')
        self.available ='unavailable'
        return super().start_driving()
    def end_trip(self):
        print(f'{self.vehicle_type}  {self.license_plate} ended ')
        self.available ='available'
        return super().end_trip()
