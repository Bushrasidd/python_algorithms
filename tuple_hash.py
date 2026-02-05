
'''
The goal of this challenge is to demonstrate an understanding of hashing and the difference between mutable (lists) and 
immutable (tuples) data structures in Python.
Task:Given an integer n (the number of elements).
Given n space-separated integers.Create a tuple t containing those n integers.
Compute and print the result of hash(t).
 '''

if __name__ == '__main__':
    n = int(input("Enter the number of elements:"))
    t = tuple(map(int, input("Enter the elements separated by space:").split()))
    print(hash(t))