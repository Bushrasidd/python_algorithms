class Animals:
    # Defult constructor which python makes for us by default such constructor only contains self parameter.
    def __init__(self):
        pass

    # Parameterized constructors which contains self along with other parameters.
    def __init__(self, name, category, height):
        print("learning classes objects and contructors")
        self.name = name
        self.category = category
        self.height = height

    
# The constructor(init func) gets revoked when an object of that class is created or initialized.
obj1 = Animals("Dog","pet",2.4)
print(obj1.name, obj1.category,obj1.height)

obj2 = Animals("Cat","pet",2.4)
print(obj2.name,obj2.category,obj2.height)

obj3 = Animals()


