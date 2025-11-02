dyn_num = int(input("Enter a num:"))
a = 0
b = 1
i = 0
c = 0

while  i <= dyn_num:
    c = a + b
    a = b
    b = c
    i += 1

print(a, end="")
    


