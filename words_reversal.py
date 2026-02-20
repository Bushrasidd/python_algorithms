#reversing the words of a string without using slicing
textt="i am improving my programming logic"
new_text = textt.split()
n = len(new_text)-1
for i in range((n)-1,-1,-1):
    print(new_text[i],end=' ')


