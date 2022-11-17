from hashlib import md5
from Brta import BRTA

license_authority = BRTA()

class User :
    def __init__(self, name , email, password) -> None:
        self.name = name 
        self.email = email 
        self.__password =password

        with open('user.txt', 'w') as file :
            pwd = self.__password.encode()
            hash_pwd = md5(pwd).hexdigest()
            file.writelines(f'{self.email} {hash_pwd}')
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


class Driver(User):
    def __init__(self, name, email, password, license , location) -> None:
        super().__init__(name, email, password)
        self.license = license
        self.location =location 
        self.earning = 0
        self.valid_driver = license_authority.check_license(self.email)
    
    def take_driving_test (self, email):
        result = license_authority.driving_test(email)
        if result :
            self.license = license_authority.license_book[email]
            self.valid_driver = True
        else :
            print("Try again")
    

               



hero_rider = User("hero", "ashik$gg.com", "123456")
hero_rider.log_in("ashik$gg.co", "12345")

kuber = Driver("kuber", "kuber@gmail.com", "121212", "12312", "dhaka")
print(kuber.valid_driver)

        