import random
import os
import json

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_random_prime(min_value, max_value):
    """Generate a random prime number in the specified range."""
    while True:
        candidate = random.randint(min_value, max_value)
        if is_prime(candidate):
            return candidate

def generate_keys(min_value, max_value):
    # Choose two large prime numbers
    p = generate_random_prime(min_value, max_value)
    q = generate_random_prime(min_value, max_value)

    # Calculate n and g
    n = p * q
    g = random.randint(2, n - 1)

    if p > q:
        p,q = q,p
    else:
        p,q = p,q

    gg = random.randint(2,q-1)

    fn = (p - 1) * (q - 1)

    e = random.randint(2, fn)

    while gcd(e, fn) != 1:
        e = random.randint(2, fn)

    # Generate private keys for Alice and Bob
    alice_private_key = random.randint(2, n - 1)
    bob_private_key = random.randint(2, n - 1)

    # Calculate public keys for Alice and Bob
    alice_public_key = pow(g, alice_private_key, n)
    bob_public_key = pow(g, bob_private_key, n)

    # Calculate shared secret keys
    alice_shared_key = pow(bob_public_key, alice_private_key, n)
    bob_shared_key = pow(alice_public_key, bob_private_key, n)

    return {
        'p': p,
        'q': q,
        'n': n,
        'g': g,
        'gg': gg,
        'e': e,
        'fn':fn,
        'alice_private_key': alice_private_key,
        'bob_private_key': bob_private_key,
        'alice_public_key': alice_public_key,
        'bob_public_key': bob_public_key,
        'alice_shared_key': alice_shared_key,
        'bob_shared_key': bob_shared_key
    }

def write(data):
    with open('data.txt', 'w') as file:
        json.dump(data, file)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def read():
    with open('data.txt', 'r') as file:
        loaded_data = json.load(file)
        return loaded_data

def print_keys(keys):
    print("Public: \tp =", keys['p'])
    print("Public: \tq =", keys['q'])
    print("Public: \tn =", keys['n'])
    print("Public: \tg =", keys['g'])
    print("Private: \tAlice's private key =", keys['alice_private_key'])
    print("Private: \tBob's private key =", keys['bob_private_key'])
    print("Public: \tAlice's public key =", keys['alice_public_key'])
    print("Public: \tBob's public key =", keys['bob_public_key'])
    print("Shared: \tAlice's shared key =", keys['alice_shared_key'])
    print("Shared: \tBob's shared key =", keys['bob_shared_key'])

def generate_and_print_keys(min_value=1000, max_value=10000):
    keys = generate_keys(min_value, max_value)
    print_keys(keys)
    write(keys)
    return keys

if __name__ == "__main__":
    generate_and_print_keys()
