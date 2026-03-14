class Invoice:
    gst = 15  #Class attributes are the attributes which stores common data for all the objects.
    def __init__(self, name, amt, date):
        self.name = name #object attributes are the attributes which stores data for each object separately.
        self.amt = amt  #object attributes have more precedence than class attributes.
        self.date = date

obj = Invoice("Karan", 30000, "25-03-2025")
print(obj.name,obj.amt,obj.date, Invoice.gst)
obj2 = Invoice("Rahul", 80000, "2-05-2025")
print(obj2.name,obj2.amt,obj2.date, Invoice.gst)

