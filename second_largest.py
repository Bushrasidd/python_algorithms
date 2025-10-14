n = int(input())
arr = list(map(int, input().split()))


largest = float('-inf')
for i in range(len(arr)):
    if arr[i]>largest:
        largest = arr[i]
    
    
sec_lar = float('-inf')

for j in range(len(arr)):
    if arr[j] > sec_lar and arr[j] != largest:
        sec_lar = arr[j]
    
print(sec_lar)