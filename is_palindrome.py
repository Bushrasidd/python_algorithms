# Give a string "Malayalam" need to check if its palindrome or  not

str0 = "MALAyalLAM"

str1 = str0.lower()
if str1 == str1[::-1]:
     print(True)
else:
     print(False)



