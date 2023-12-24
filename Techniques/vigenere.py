def vigenere_transform(char, key_char, reverse=False):
    case_diff = ord('a') - ord('A')
    char_base = ord('A') if char.isupper() else ord('a')

    shift = (ord(key_char) - ord('A')) if key_char.isupper() else (ord(key_char) - ord('a'))
    if reverse:
        shift = -shift

    encrypted_char = chr((ord(char) - char_base + shift) % 26 + char_base)
    return encrypted_char

def vigenere_encrypt(plaintext, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            result += vigenere_transform(char, key[key_index % len(key)])
            key_index += 1
        else:
            result += char

    return result

def vigenere_decrypt(ciphertext, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            result += vigenere_transform(char, key[key_index % len(key)], reverse=True)
            key_index += 1
        else:
            result += char

    return result

# Take plaintext input from user
plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")

# Encrypt and decrypt
ciphertext = vigenere_encrypt(plaintext, key)
decrypted_text = vigenere_decrypt(ciphertext, key)

# Display results
print(f"Plaintext: {plaintext}")
print(f"Key: {key}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")
