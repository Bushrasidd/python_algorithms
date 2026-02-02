def calc():
    print("Hii User Welcome to Calculator")
    num1 = int(input("Enter the first num:"))
    num2 = int(input("Enter the second num:"))
    Op = input("Enter the Opearations to be performed:")
    if Op == "+":
        num3 = num1+num2
    elif Op == "-":
        num3 = num1-num2
    elif Op == "*":
        num3 = num1*num2
    elif Op == "//":
        num3 = num1//num2
    return num3
result = calc()
print(result)




