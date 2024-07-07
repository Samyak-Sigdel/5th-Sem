
def vigenere_encrypt(text, key):
    encrypted_text = []
    key_len = len(key)
    
    for i in range(len(text)):
        j = i % key_len
        
        if text[i].isalpha():
            if text[i].isupper():
                encrypted_char = chr((ord(text[i]) - ord('A') + ord(key[j].lower()) - ord('a')) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(text[i]) - ord('a') + ord(key[j].lower()) - ord('a')) % 26 + ord('a'))
        else:
            encrypted_char = text[i]
        
        encrypted_text.append(encrypted_char)
    
    return ''.join(encrypted_text)

def vigenere_decrypt(text, key):
    decrypted_text = []
    key_len = len(key)
    
    for i in range(len(text)):
        j = i % key_len
        
        if text[i].isalpha():
            if text[i].isupper():
                decrypted_char = chr((ord(text[i]) - ord('A') - (ord(key[j].lower()) - ord('a')) + 26) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(text[i]) - ord('a') - (ord(key[j].lower()) - ord('a')) + 26) % 26 + ord('a'))
        else:
            decrypted_char = text[i]
        
        decrypted_text.append(decrypted_char)
    
    return ''.join(decrypted_text)

def main():
    text = input("Enter the text : ")
    key = input("Enter the key : ")

    encrypted_text = vigenere_encrypt(text, key)
    print("Encrypted text:", encrypted_text)
    
    decrypted_text = vigenere_decrypt(encrypted_text, key)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
