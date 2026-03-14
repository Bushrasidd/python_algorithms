class Invoice:
    def __init__(self, name, amt, date):
        self.name = name
        self.amt = amt
        self.date = date

obj = Invoice("Karan", 30000, "25-03-2025")
print(obj.name,obj.amt,obj.date)
obj2 = Invoice("Rahul", 80000, "2-05-2025")
print(obj2.name,obj2.amt,obj2.date)