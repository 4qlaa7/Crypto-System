#!/usr/bin/env python
# coding: utf-8

# In[18]:


import random

def mod_exp(f, h):
    result = f % h
    return result



def generate_keypair():
    
    q = int(input("Enter prime number (q): "))
    a = int(input("Enter primitive root (a): "))

    
    x = int(input(f"Enter a private key number between 2 and {q - 2}: "))

   
    y = mod_exp(a^x, q)

    return (q, a, x), (q, a, y)


def encrypt(public_key, plaintext):
    q, a, y = public_key

    k = int(input(f"Enter a k  number between 2 and {q - 2}: "))

    if k <= 2 or k >= q :
        print("Invalid input. Please enter a number between 2 and q - 2.")
        return None

    
    c1 = mod_exp(a**k, q)
    gg = mod_exp(y**k,q)
    c2 = mod_exp(gg**plaintext, q)

    return c1, c2

def decrypt(private_key):
    q, a, x = private_key
    c1 = int(input("first ciphertext "))
    c2 = int(input("secound ciphertext "))
    ciphertext= c1, c2 
    
    s = mod_exp(c1** x, q)

   
    s_inv =mod_exp(q, c1** x)*s


  
    decrypted_message = mod_exp(q,c2 * s_inv)

    return decrypted_message



private_key, public_key = generate_keypair()
u = input(f"Enter a operation ")



if u == 'e':
    
    plaintext = int(input("m: "))
    print("Original message:", plaintext)

    ciphertext = encrypt(public_key, plaintext)
    print("Encrypted message (c1, c2):", ciphertext)




if u == 'd':
    
    decrypted_message = decrypt(private_key)  # Assuming ciphertext is defined
    print("Decrypted message:", decrypted_message)


# In[ ]:





# In[ ]:





# In[ ]:




