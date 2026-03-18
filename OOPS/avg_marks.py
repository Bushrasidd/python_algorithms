class Student:
    def __init__(self, name, list1):
        self.name = name
        self.marks = list1
    def average(self):
        total = 0
        for val in self.marks:
            total+=val
        avg = total/len(self.marks)
        return avg
    
        
list1 = [45.75,88,95]
s1 = Student("Rahul", list1)
s1.name = "Karan" #object attributes have more precedence than class attributes.
print("Average marks of", s1.name, "is:", s1.average())

