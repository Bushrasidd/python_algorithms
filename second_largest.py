# Given the scores for a set of participants, find the score of the runner-up.

# The scores may include duplicates.

# The runner-up is defined as the second highest unique score in the list.

# Input Format
# The first line contains an integer, n, the number of scores.

# The second line contains an array of n integers separated by a space, representing the scores.

# Constraints
# 2 ≤ n ≤ 10
# −100 ≤ A[i] ≤ 100 (Note: The scores can be negative)

# Hence Need to find second largest


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
