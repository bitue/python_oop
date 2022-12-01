from hashlib import md5
import Brta as b
from Vichele import Car, Bike, Cng
from ride_manager import uber

license_authority = b.BRTA()

class User :
    def __init__(self, name , email, password) -> None:
        self.name = name 
        self.email = email 
        self.__password =password 

        with open('user.txt', 'a') as file :
            pwd = self.__password.encode()
            hash_pwd = md5(pwd).hexdigest()
            file.writelines(f' {self.email} {hash_pwd} \n')
            file.close()
    
    @staticmethod
    def log_in(email, password):
        with open("user.txt", 'r') as file :
            lines = file.readlines()
            get_password = ""
         
            for line in lines :
                if email == line.split(" ")[0]:
                    get_password = line.split(" ")[1]
                else :
                    print("Invalid email")
                    file.close()
                    return 
            
            file.close()
        
        if md5(password.encode()).hexdigest() == get_password :
            print("Valid User")
        else :
            print("Invalid password") 
               

class Traveler (User):
    def __init__(self, name, email, password, location, balance) -> None:
        self.location =location
        self.balance = balance
        super().__init__(name, email, password)
    
    def set_location (self , location):
        self.set_location =location
    
    def get_location(self):
        return self.location
    def request_trip(self, location):
        pass 

    def start_trip(self, fare):
        self.balance -= fare
        pass

class Driver(User):
    def __init__(self, name, email, password, location) -> None:
        super().__init__(name, email, password)
        self.location =location
        self.license = license_authority.check_license(email)
        self.earn =0 
        self.valid_driver = license_authority.valid_driver(self.email)
    
    def start_a_trip(self, destination, fare):
        self.location = destination
        self.earn +=fare
    
    def test_driving_license(self, email):
        res = license_authority.driving_test(email)
        if res :
            print("success")
            self.license = license_authority.license_book[email]
            self.valid_driver = True
            print(license_authority.license_book)
        else :
            print("Try Again ")
    
    def add_vehicle(self, vehicle_type, license_plate, rate):
        if self.valid_driver :
            if vehicle_type =='car':
                new_vehicle = Car(vehicle_type, license_plate, rate, self.email)
                uber.add_available_vehicle(new_vehicle.vehicle_type, new_vehicle)
                print("added a vehicle")
            elif vehicle_type =='bike':
                new_vehicle = Bike(vehicle_type, license_plate, rate, self.email)
                uber.add_available_vehicle(new_vehicle.vehicle_type, new_vehicle)
                print("added a vehicle")
            elif vehicle_type =='cng':
                new_vehicle = Cng(vehicle_type, license_plate, rate, self.email)
                uber.add_available_vehicle(new_vehicle.vehicle_type, new_vehicle)
                print("added a vehicle")
        else :
            print("You are not allowed to get vehicle")

# hero_rider = User("hero", "ashik$gg.com", "123456")
# hero_rider.log_in("ashik$gg.co", "12345")

driver_one = Driver("ash", "kub@gg.com", "mirpor", "120002")
driver_one.test_driving_license(driver_one.email)
driver_one.add_vehicle('car', "12-9090",12)


driver_t = Driver("ash", "kb@gg.com", "mipor", "12002")
driver_t.test_driving_license(driver_t.email)
driver_t.add_vehicle('bike', "12-909",902)


print(driver_one.license)
print(driver_one.valid_driver)
print(uber.available_cars, uber.available_bikes )

path = '/user.txt'
del path



