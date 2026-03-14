# HAckerRank - The Minion Game
# The Minion Game is a word game involving two players, Stuart and Kevin. Both players
# are given the same string, and they have to make substrings using the letters of the string.
# Stuart has to make words starting with consonants, and Kevin has to make words starting with vowels. The game ends when both players have made all possible substrings. The player with the most substrings wins.
# Scoring: Each occurrence of a substring adds 1 point to the player's score
# solution: We can solve this problem by iterating through the string and counting the number of substrings that can be formed starting with each character. For each character, we can calculate the score based on whether 
# it is a vowel or a consonant and keep track of the scores for both players. Finally, we can compare the scores and determine the winner.
# Complexity Time: O(n) — We only loop through the string once.Space: O(1) — We only store two integer scores.

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


    # (Select CITY from STATION ORDER BY LENGTH(CITY) ASC, CITY ASC LIMIT 1) UNION ALL(Select CITY from STATION ORDER BY LENGTH(CITY) DESC, CITY DESC LIMIT 1);