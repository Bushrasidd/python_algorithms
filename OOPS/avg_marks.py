class Student:
    def __init__(self, name, list1):
        self.name = name # object attributes also called instance attributes are the attributes which stores data for each object separately. 
        self.marks = list1
    @staticmethod
    def welcome():
        print("Welcome to the world of OOPS")
    def average(self):
        total = 0
        for val in self.marks:
            total+=val
        avg = total/len(self.marks)
        return avg
    
    
        
list1 = [45.75,88,95]
s1 = Student("Rahul", list1) #object also called instances created from class each object have their own unique data called object attribute or instance attributes.
s1.name = "Karan" #object attributes have more precedence than class attributes.
s1.welcome()
print("Average marks of", s1.name, "is:", s1.average())


