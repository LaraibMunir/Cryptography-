def caesar_cipher_encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

plaintext = "HELLO"
shift = 3
ciphertext = caesar_cipher_encrypt(plaintext, shift)
print("Encrypted:", ciphertext)
print("Decrypted:", caesar_cipher_decrypt(ciphertext, shift))
  
