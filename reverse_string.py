# Reverse a string without using prebuilt functions

org_string = input("Enter a string:")

# rev_str = org_string[::-1]

# print(rev_str)

i = len(org_string)-1

while i >=0:
    print(org_string[i], end="")
    i -= 1
