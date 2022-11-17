class Account :
    acc_id = 1 # class attribute 
    def __init__(self, name, age , nid, balance ) :
        self.name =name
        self.age =age
        self.nid =nid
        self.balance = balance
        self.account_id = Account.acc_id 
        Account.acc_id+=1 
    
    def deposit(self, amount):
        if(amount >=0):
            self.balance += amount
        else :
            print("Invalid")
            return
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -=amount
        else :
            print("Invalid ")
            return 
    


if __name__=="main":   
  

    acc_1 = Account("Ash", 12, 233, 2000)
    acc_2 = Account("Ash", 12, 233, 2000)

    

        