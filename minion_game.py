def minion_game(string):
    vowels = "AEIOU"
    stuart_const_score = 0
    Kevin_vow_score = 0
    n = len(string)
    for i in range(n):
        score = n-i
        if string[i] in vowels:
            Kevin_vow_score += score
        else:
            stuart_const_score += score
    if Kevin_vow_score > stuart_const_score:
        print(f"Kevin {Kevin_vow_score}")
    elif Kevin_vow_score < stuart_const_score:
        print(f"Stuart {stuart_const_score}")
    else:
        print("Draw")   
    

if __name__ == '__main__':
    s = input()
    minion_game(s)