alphabets_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

def rotN(c,N):
    pos=alphabets_list.find(c)
    if pos== -1 :
        return c
    else :
        return alphabets_list[pos + N]

def encoderRotN(s , N) :
    return "".join([rotN(ch, N) for ch in s])

def rot13(s) :
    return encoderRotN(s , 13)

print(rot13("abcd"))    
