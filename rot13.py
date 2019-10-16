alphabets_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rot13_encrypt(plain_text) :
    encrypted_text=[]
    for alphabet in plain_text :
        if alphabets_list.find(alphabet) < 26 :
            encrypted_text.append(alphabets_list[(alphabets_list.find(alphabet) + 13) % 26])
        else :
            encrypted_text.append(alphabets_list[((alphabets_list.find(alphabet) + 13) % 26) + 26])
    return "".join(encrypted_text)

def rot13_decrypt(cypher_text) :
    return rot13_encrypt(rot13_encrypt(cypher_text))

cypher_text = "abyzABYZ"

print(rot13_encrypt(cypher_text))
print(rot13_decrypt(cypher_text))
