class Invoice:
    gst = 15  #Class attributes are the attributes which stores common data for all the objects.
    def __init__(self, name, amt, chr, date):
        self.name = name #object attributes are the attributes which stores data for each object separately.
        self.amt = amt  #object attributes have more precedence than class attributes.
        self.chr = chr
        self.date = date
    def charges_cal(self,amt,chr):
        return chr+(amt*Invoice.gst/100)

obj = Invoice("Karan", 30000, 500, "25-03-2025")
print(obj.name,obj.amt,obj.date, obj.chr, Invoice.gst)

t1 = obj.charges_cal(obj.amt, obj.chr)
print("tax payable for Karan:", t1)
obj2 = Invoice("Rahul", 80000, 400, "2-05-2025")
print(obj2.name,obj2.amt,obj2.date, obj2.chr, Invoice.gst)
t2 = obj2.charges_cal(obj2.amt, obj2.chr)
print("tax payable for Rahul:", t2)
