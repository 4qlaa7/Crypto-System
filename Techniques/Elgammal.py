

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


def elg_encrypt(p,q,g,public, plaintext):
    
    if p > q:
        p,q = q,p
    else:
        p,q = p,q
        

    k = g

    if k <= 2 or k >= q :
        print("Invalid input. Please enter a number between 2 and q - 2.")
        return None , None


    y = public
    c1 = mod_exp(p**k, q)
    gg = mod_exp(y**k,q)
    c2 = mod_exp(gg*plaintext, q)

    
    return c1,c2


def elg_decrypt(p,q,c1,c2,private_key):
    q, a = q , p
    c1 = int(c1)
    c2 = int(c2)
    
    if a > q:
        a,q = q,p
    else:
        a,q = p,q
    x = private_key
    
    s = mod_exp(c1** x, q)

   
    s_inv =mod_exp(q, c1** x)*s


  
    decrypted_message = mod_exp(q,c2 * s_inv)

    return decrypted_message






