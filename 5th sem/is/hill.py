def mod_inverse(a, m):
    m0, t, x0, x1 = m, 0, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        t, x0 = x0, x1 - q * x0
        x1 = t
    if x1 < 0:
        x1 += m0
    return x1

def matrix_mod_inv(matrix, mod):
    det = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % mod
    if det == 0 or gcd(det, mod) != 1:
        raise ValueError("The key matrix is not invertible.")
    det_inv = mod_inverse(det, mod)

    adjugate = [
        [matrix[1][1], -matrix[0][1]],
        [-matrix[1][0], matrix[0][0]]
    ]

    for i in range(2):
        for j in range(2):
            adjugate[i][j] = (adjugate[i][j] * det_inv) % mod
            if adjugate[i][j] < 0:
                adjugate[i][j] += mod

    return adjugate

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def encrypt(plaintext, key):
    len_plaintext = len(plaintext)
    plaintext = plaintext.lower()
    cipher = []

    for i in range(0, len_plaintext, 2):
        if i + 1 >= len_plaintext:
            break
        vector = [ord(plaintext[i]) - ord('a'), ord(plaintext[i + 1]) - ord('a')]
        result = [
            (key[0][0] * vector[0] + key[0][1] * vector[1]) % 26,
            (key[1][0] * vector[0] + key[1][1] * vector[1]) % 26
        ]
        cipher.append(chr(result[0] + ord('a')))
        cipher.append(chr(result[1] + ord('a')))

    return ''.join(cipher)

def decrypt(cipher, key):
    len_cipher = len(cipher)
    cipher = cipher.lower()
    plaintext = []

    key_inv = matrix_mod_inv(key, 26)

    for i in range(0, len_cipher, 2):
        if i + 1 >= len_cipher:
            break
        vector = [ord(cipher[i]) - ord('a'), ord(cipher[i + 1]) - ord('a')]
        result = [
            (key_inv[0][0] * vector[0] + key_inv[0][1] * vector[1]) % 26,
            (key_inv[1][0] * vector[0] + key_inv[1][1] * vector[1]) % 26
        ]
        plaintext.append(chr(result[0] + ord('a')))
        plaintext.append(chr(result[1] + ord('a')))

    return ''.join(plaintext)

def main():
    plaintext = input("Enter plaintext: ").replace(" ", "").lower()
    key = []
    print("Enter key matrix (2x2, space-separated):")
    for i in range(2):
        row = list(map(int, input().split()))
        key.append(row)

    try:
        encrypted_text = encrypt(plaintext, key)
        print("Encrypted text:", encrypted_text)

        decrypted_text = decrypt(encrypted_text, key)
        print("Decrypted text:", decrypted_text)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
