#!/usr/bin/env python
# coding: utf-8

# In[8]:


import random

def mod_exp(f, h):
    result = f % h
    return result

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        q, x, y = extended_gcd(b % a, a)
        return q, y - (b // a) * x, x

def mod_inverse(a, m):
    _, x, _ = extended_gcd(a, m)
    return x % m if x >= 0 else (x % m + m) % m


def generate_keypair():
    # Step 1: Choose large prime numbers q and a
    q = int(input("Enter prime number (q): "))
    a = int(input("Enter primitive root (a): "))

    # Step 2: Choose private key x
    x = int(input(f"Enter a private key  number between 2 and {q - 2}: "))


    # Step 3: Compute public key y
    y = mod_exp(a^x, q)

    return (q, a, x), (q, a, y)

def encrypt(public_key, plaintext):
    q, a, y = public_key

    k = int(input(f"Enter a k  number between 2 and {q - 2}: "))

    if k <= 2 or k >= q :
        print("Invalid input. Please enter a number between 2 and q - 2.")
        return None

    # Step 2: Compute c1 and c2
    c1 = mod_exp(a^k, q)
    gg=mod_exp(y^k,q)
    c2 = mod_exp(gg*plaintext, q)

    return c1, c2

def decrypt(private_key, ciphertext):
    q, a, x = private_key
    c1, c2 = ciphertext
    # Compute s
    s = mod_exp(c1^ x, a)

    # Compute s^-1
    s_inv = mod_inverse(s , q)

    # Decrypt the message
    decrypted_message = (c2 * (s_inv % q))

    return decrypted_message

# Example
private_key, public_key = generate_keypair()
plaintext = int(input("m: "))
print("Original message:", plaintext)

operation_o = input("Enter the operation (o): ")

if operation_o == 'e':
    # Encryption
    ciphertext = encrypt(public_key, plaintext)
    print("Encrypted message (c1, c2):", ciphertext)

# User input for operation 'f'
operation_f = input("Enter the operation (f): ")

if operation_f == 'd':
    # Decryption
    decrypted_message = decrypt(private_key, ciphertext)  # Assuming ciphertext is defined
    print("Decrypted message:", decrypted_message)


# In[ ]:





# In[ ]:





# In[ ]:




