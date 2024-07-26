import random
from sympy import isprime, mod_inverse

# Generate a large prime number
def generate_prime(bits=512):
    while True:
        num = random.getrandbits(bits)
        if isprime(num):
            return num

# RSA key generation
def generate_rsa_keys(bits=512):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = 65537  # Common choice for e
    d = mod_inverse(e, phi)  # Compute d using modular inverse
    
    return {
        'public': (e, n),
        'private': (d, n)
    }

# RSA encryption
def rsa_encrypt(plaintext, public_key):
    e, n = public_key
    return pow(plaintext, e, n)

# RSA decryption
def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    return pow(ciphertext, d, n)

# Example usage
keys = generate_rsa_keys(bits=256)
public_key = keys['public']
private_key = keys['private']

plaintext = 12345  # Example plaintext message (as an integer)
print("Original plaintext:", plaintext)

ciphertext = rsa_encrypt(plaintext, public_key)
print("Encrypted ciphertext:", ciphertext)

decrypted_plaintext = rsa_decrypt(ciphertext, private_key)
print("Decrypted plaintext:", decrypted_plaintext)
  
