from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import time
import hashlib

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789. "

def bytes_to_6bit_chunks(data: bytes) -> str:
    bits = 0
    bits_left = 0
    output = []
    for byte in data:
        bits = (bits << 8) | byte
        bits_left += 8
        while bits_left >= 6:
            bits_left -= 6
            chunk = (bits >> bits_left) & 0x3F
            output.append(letters[chunk])
    if bits_left > 0:
        chunk = (bits << (6 - bits_left)) & 0x3F
        output.append(letters[chunk])
    return "".join(output)

def encrypt(plaintext: str, key: bytes) -> bytes:
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, plaintext.encode(), None)
    return nonce + ciphertext

def main():
    passphrase = "SUpErSeCCuReKEyFoRMySeCRETMEssaGe!. "
    key = hashlib.sha256(passphrase.encode()).digest()  # 256-bit key

    message = input("Enter message to encrypt: ")
    encrypted_bytes = encrypt(message, key)
    encoded_string = bytes_to_6bit_chunks(encrypted_bytes)

    print(f"Encoded encrypted message:\n{encoded_string}")

if __name__ == "__main__":
    main()
