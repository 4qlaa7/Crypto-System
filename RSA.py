import random
import math

def primes_in_range(x, y):
    prime_list = []
    for n in range(x, y):
        is_prime = True

        for num in range(2, int(math.sqrt(n)) + 1):
            if n % num == 0:
                is_prime = False
                break

        if is_prime:
            prime_list.append(n)

    return prime_list

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError("Modular inverse does not exist")
    else:
        return x % m

def powmod(b, e, m):
    r = 1
    b = b % m
    if b == 0:
        return 0
    while e > 0:
        if e % 2:
            r = (r * b) % m
        e = e >> 1
        b = (b * b) % m
    return r

def generate_keypair():
    prime_list = primes_in_range(5000, 10000)
    p = random.choice(prime_list)
    q = random.choice(prime_list)
    n = p * q
    fn = (p - 1) * (q - 1)
    e = random.randint(2, fn)
    while math.gcd(e, fn) != 1:
        e = random.randint(2, fn)
    d = mod_inverse(e, fn)
    public_key = (e, n)
    private_key = (d, n)
    print("Q is: ", q)
    print("P is: ", p)
    print("N is :",n)
    print("FN is:",fn)
    print('e is:',e)
    print('d is:',d)
    return public_key, private_key

def encrypt(message, public_key):
    e, n = public_key
    if isinstance(message, str):
        encrypted_message = [powmod(ord(char), e, n) for char in message]
    elif isinstance(message, int):
        encrypted_message = powmod(message, e, n)
    else:
        raise ValueError("Input type not supported")
    return encrypted_message

def decrypt(encrypted_message, private_key):
    d, n = private_key
    if isinstance(encrypted_message, list):
        decrypted_message = ''.join([chr(powmod(char, d, n)) for char in encrypted_message])
    elif isinstance(encrypted_message, int):
        decrypted_message = powmod(encrypted_message, d, n)
    else:
        raise ValueError("Input type not supported")
    return decrypted_message

public_key, private_key = generate_keypair()
print("Public key:", public_key)
print("Private key:", private_key)

# Encrypt text
original_text = 'ahmedjhgfds98765'
print("Original text:", original_text)
encrypted_text = encrypt(original_text, public_key)
print("Encrypted text:", encrypted_text)
decrypted_text = decrypt(encrypted_text, private_key)
print("Decrypted text:", decrypted_text)



