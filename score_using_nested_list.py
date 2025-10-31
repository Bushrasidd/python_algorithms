# This problem requires processing student data, stored as a nested list of 
# [name, grade] pairs, to identify the second lowest unique grade achieved in the class.

# The final output must list the names of all students who achieved this 
# second lowest grade, ordered alphabetically, with each name on a new line.


n = int(input())
a = []

for i in range(n):
    name = input()
    while True:
        try:
            marks = float(input())
            break
        except ValueError:
            print("invalid input")
    
    student_record = [name, marks]
    
    a.append(student_record)
   
    

low = a[0][1]    
for i in range(len(a)):
    if a[i][1] <low:
        low = a[i][1]
    

sec_low = None 
for j in range(len(a)):
    if a[j][1] != low:
        if sec_low is None or a[j][1]< sec_low:
             sec_low = a[j][1]
            
        
lowest_record = []        
for student_record in a:
    if student_record[1] == sec_low:
        lowest_record.append(student_record[0])


lowest_record.sort()        
        
for name in lowest_record:
    print(name)   

