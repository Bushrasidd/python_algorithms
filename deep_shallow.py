import copy

#Shallow copy copies the refrence of the object any changes made to the original object will reflect in the
#  copied object as well as long as it is nested with one or more mutable objects. if it does not contain any mutable objects then it will work as deep copy.
num = [[3,4,5,6],[7,8,9,10]]
new_list = copy.copy(num)
num[0][1] = 55
new_list[1][1] = 100
print(new_list)


#Deep copy creates a new object and recursively adds the copies of nested objects present in the 
# original elements. Any changes made to the original object will not reflect in the copied object.
fruits = ["apple","banana","manago","cherry","kiwi"]
fr = copy.deepcopy(fruits)
fruits[2] = "litchi"
print (fruits)
print(fr)
