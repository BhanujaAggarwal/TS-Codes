import string
all_alphabets = set(string.ascii_lowercase)

def generate_common_letters (word_guess, player1) :
    common_letters = list(set(word_guess) & set(player1))
    return common_letters

def proceed(word_guess, player1) :
    common_letters = generate_common_letters(word_guess, player1)
    score = len(common_letters)
    if score == 0 :
        all_alphabets.discard(common_letters)
        return "0"
    elif score == 4 :
        if word_guess == player1 :
            return "You win"
        else :
            return "4, Anagram"

    return "1,2,3"

def is_valid_guess(word1) :
    for alphabet in word1 :
        if (alphabet not in all_alphabets) :
            return False
    return True

def get_word(player1) :
    file1 = open("sowpods.txt","r")
    contents =file1.readlines()
    for x in contents :
    	word1 = x.strip()
        if len(word1) == 4 and is_valid_guess(word1):
            temp = proceed(word1, player1)
            if temp == "You win" :
                print("You win")
                break
            else :
                print("ahasndjn")

player1 = "abas"
get_word(player1)
