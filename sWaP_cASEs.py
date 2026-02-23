#The goal is to take a given string and toggle the case of every alphabetic character—converting uppercase to lowercase 
# and lowercase to uppercase. The strings in python are immutable, which means we cannot change them directly. To achieve this, 
# we can convert the string into a list of characters, modify the cases as needed, and then join the list back into a string.

def swap_case(s):
    new_s = list(s)
    list1 = []
    i=0
    for i in range(len(new_s)):
        if new_s[i].isupper():
            list1.append(new_s[i].lower())
        else:
            list1.append(new_s[i].upper())
    return ''.join(list1)
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)