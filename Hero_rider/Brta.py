import random
import hashlib

class BRTA:
    license_book ={}

    def __init__(self) -> None:
        pass

    def driving_test(self, email):
        score = random.randint(20, 100)
        if score >=33 :
            license_num = str(random.randint(1000, 5000)) 
            has_license = hashlib.md5(license_num.encode()).hexdigest()
            BRTA.license_book[email] = has_license
            print("License done successful !!!")
            return True
        
        else :
            print("Try Again !")
            return False
    
    def check_license (self, email):
        try :
            if BRTA.license_book[email] :
                return BRTA.license_book[email]
        except:
            return False
    
    def valid_driver(self, email):
        try :
            if email in BRTA.license_book :
                return True
            else :
                return False
        
        except:
            return False 
    
   
            
    
     
