
#Find second largest number in a list withou using set.

list1 = [20,10,40,10,5,20,5]

lar = []

for i in range(len(list1)):
    if list1[i] not in lar:
        lar.append(list1[i])
print(lar)

lar.sort()
print(lar[-2])

# Find the largest number in a list. without using Max function.

list1 = [20,10,40,10,5,20,5]
largest = list1[0]
for i in range(1, len(list1)):
    if largest < list1[i]:
        largest = list1[i]
    
print(largest)

# Find the frequency of each character in a string.

string = "people"

f = {}
for i in string:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
print(f)



