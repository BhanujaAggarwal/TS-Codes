alphabets_list = "abcdefghijklmnopqrstuvwxyz"

def rot13_encrypt(plain_text) :
    return "".join ( [alphabets_list[(alphabets_list.find(alphabet) + 13) % 26] for alphabet in plain_text] )

def rot13_decrypt(cypher_text) :
    return rot13_encrypt(rot13_encrypt(cypher_text))

plain_text = "abcdefghijklmnopqrstuvwxyz"
print (rot13_encrypt(plain_text))
print (rot13_decrypt(plain_text))
