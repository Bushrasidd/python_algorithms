# Given the names and marks of N students, store them in a dictionary 
# where each student’s name maps to a list of their marks. 
# Then, given a student’s name, calculate and display their average marks rounded to two decimal places.

# INPUT

# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika

# OUTPUT = 56.00


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    query_name = input()
    
    if query_name in student_marks:
        avg = sum(student_marks[query_name])/len(student_marks[query_name])
        print(f"{avg:.2f}")