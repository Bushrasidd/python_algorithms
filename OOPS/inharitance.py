class Employee:
    def __init__(self, name, salary, department,Bank_details):
        self.name = name
        self.salary = salary
        self.department = department
        self.Bank_details = Bank_details
        print(Bank_details)

    @staticmethod
    def title():
        print("Employes Details")
Bank_details = {"acc_no":2584655,"ifsc":"IFSCKAR00B"}
print(type(Bank_details))
emp1 = Employee("Rahul", 20000, "Sales", Bank_details)
emp1.title()
print(emp1.name,emp1.salary,emp1.department, emp1,Bank_details)
del emp1.name #Del keyword is used to create the object property and object itself.
# print(emp1.name,emp1.salary,emp1.department)