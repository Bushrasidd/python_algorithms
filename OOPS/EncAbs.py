#Abstraction in python refers to the concept of hiding the internal details of a class and object and exposing only essential details to the outside world.
#Encapsulation in OOPS is a practice to bundle function and data in a single unit to perform specific operation.
class Account:
    def __init__(self, acc_num, bal):
        self.acc_num = acc_num
        self.bal = bal

    def debit(self, ammount):
        self.bal-=ammount
        print(f"your account is been debited for {ammount}rs.")

    def credit(self, ammount):
        self.bal+=ammount
        print(f"your account has been credited for {ammount}rs.")
    
    def print(self):
        return self.bal

s1 = Account("00125",1000)
s1.debit(500)
s1.credit(800)
print(f"Current balance is {s1.bal}")
    