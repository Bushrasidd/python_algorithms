n = int(input("Enter the number of students: "))

a = []

for i in range(n):
    name = input("Enter the name of student: ")
    while True:
        try:
            marks = int(input("Enter the marks of student: "))
            break
        except ValueError:
            print("invalid input")
    
    student_record = [name, marks]
    
    a.append(student_record)
    print("list of student records is : ", a)
    

low = a[0][1]    
for i in range(n-1):
    if a[i][1] <low:
        low = a[i][1]
    

sec_low = a[0][1] 
for j in range(n-1):
    if a[j][1] < a[j+1][1] and a[j][1] != low:
        sec_low = a[j][1]

print("The second lowest marks are: ", sec_low)
print("the lowest marks are: ", low)