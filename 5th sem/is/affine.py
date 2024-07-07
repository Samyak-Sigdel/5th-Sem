import sys

# Function to calculate gcd of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find modular inverse using extended Euclidean algorithm
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None  # Modular inverse does not exist

# Function to encrypt a message using Affine Cipher
def encrypt(message, a, b):
    encrypted_message = []
    for char in message:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr(((a * (ord(char) - ord('a')) + b) % 26) + ord('a'))
            else:
                encrypted_char = chr(((a * (ord(char) - ord('A')) + b) % 26) + ord('A'))
            encrypted_message.append(encrypted_char)
        else:
            encrypted_message.append(char)
    return ''.join(encrypted_message)

# Function to decrypt a message using Affine Cipher
def decrypt(message, a, b):
    decrypted_message = []
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        print("Modular inverse does not exist. Decryption failed.")
        sys.exit(1)
    for char in message:
        if char.isalpha():
            if char.islower():
                decrypted_char = chr((a_inv * (ord(char) - ord('a') - b + 26) % 26) + ord('a'))
            else:
                decrypted_char = chr((a_inv * (ord(char) - ord('A') - b + 26) % 26) + ord('A'))
            decrypted_message.append(decrypted_char)
        else:
            decrypted_message.append(char)
    return ''.join(decrypted_message)

# Main function to handle user input and execute encryption/decryption
def main():
    message = input("Enter message : ")
    a = int(input("Enter key 1: "))
    if gcd(a, 26) != 1:
        print("'a' and 26 are not coprime. Please choose another 'a' value.")
        sys.exit(1)
    b = int(input("Enter key 2: "))
    
    encrypted_message = encrypt(message, a, b)
    print("Encrypted message:", encrypted_message)
    
    decrypted_message = decrypt(encrypted_message, a, b)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()

