# *args in python are used to pass the non-keyword arbitrary number to a function like array or list
# **kwargs args in python are used to pass the keyword arbitrary number to a function like dict

# generators in python are kind of function which displays one value at a time, initially it just returns the 
# the generator object then iterating that what gives as the value. it pauses the function and 
# and yield one value at a time execute or resume for second when it is explicitly called.
# they can be define by giving exp in () or by using function keyword def and yield.

# METHOD:1

org_list = [4,5,6,7]

list1 = (x*x for x in org_list)

list_from_generators = list(list1)

print(list_from_generators)

# METHOD:2

def even_num(numbers):
    for i in numbers:
        if i%2 == 0:
            yield i
            i += 1

numbers = [8,7,6,12,15]

list2 = even_num(numbers)

for num in list2:
    print(num)


# List comprehension is a way of applying new methods or extracting a new list based on existing list

# syntax:
# name = [exp for item in iterable if condition]

org_list = [4,5,6,7]

list1 = [x*x for x in org_list]

print(list1)



