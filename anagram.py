def check_anagram(word1,word2) :
    # word1_final = ''.join(word1.split())
    # word1_final= sorted(word1)
    # word2_final = ''.join(word2.split())
    # word2_final= sorted(word2)
    # word1_final=list(sorted(word1))
    # word2_final=list(sorted(word2))
    # word1_final1=word1_final.remove(' ')
    # word2_final2=word2_final.resortmove(' ')
    # print(word1_final)
    # print(word2_final2)

    # word1_final = ''.join(str((sorted(word1))).split())
    # word2_final = ''.join(str((sorted(word2))).split())
    # word1_final=(str(sorted(word1))).remove(" ")
    # word2_final=(str(sorted(word2))).replace(" ","")
    word1_final = sorted(word1)
    word2_final = sorted(word2)

    return word1_final==word2_final

word1="abc d"
word2="dcba"

if check_anagram(word1,word2) :
    print("Yes")
else :
    print("No")
