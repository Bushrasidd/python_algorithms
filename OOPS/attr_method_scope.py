
# Conceptual Implimentation in Python

class UserAccount:
    name = "anonymous"
    def __init__(self, acc_num, acc_pass,name):
        self.name = name
        self.acc_num = acc_num
        self.__acc_pass = acc_pass # __can be used to make the object attributes private which are only accessible inside the respective class and functions defined in it.

    def __change_password(self):
        print(self.__acc_pass)

    def x(self):
        self.__change_password()

user = UserAccount("neha",12345678, "SCKAR00B")
print(user.name,user.acc_num)
# user.change_password() 
user.x() #we can call the private functions indirectly.
       