# Give a string "Malayalam" need to check if its palindrome or not

str0 = "MALAyalLAM"

str1 = str0.lower()
if str1 == str1[::-1]:
     print(True)
else:
     print(False)

# Get a first non repeating character in a string.

str2 = "people"
freq = {}
for i in str2:
     if i in freq:
          freq[i]+=1
     else:
          freq[i]=1

for i in freq:
     if freq[i]==1:
          print(i)



         







