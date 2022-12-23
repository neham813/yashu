def encrypt (text,s):
    result =" "
    for i in range(len(text)):
        char = text[i]
        if(char.isupper()):
            result +=chr((ord(char)+s-65)%26+65)
        else:
            result +=chr((ord(char)+s-95)%26+95)
    return result
text="ATTACK AT ONCE"
s=4
print("text:",text)
print("shift:",str(s))
print("cipher:",encrypt(text,s))
                    