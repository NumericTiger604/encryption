from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import hashlib
import time

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789. "

def sixbit_string_to_bytes(s: str) -> bytes:
    bits = 0
    bits_left = 0
    output = bytearray()
    for char in s:
        chunk = letters.index(char)
        bits = (bits << 6) | chunk
        bits_left += 6
        while bits_left >= 8:
            bits_left -= 8
            byte = (bits >> bits_left) & 0xFF
            output.append(byte)
    return bytes(output)

def decrypt(encrypted: bytes, key: bytes) -> str:
    nonce = encrypted[:12]
    ciphertext = encrypted[12:]
    aesgcm = AESGCM(key)
    plaintext = aesgcm.decrypt(nonce, ciphertext, None)
    return plaintext.decode()

def slow_print(text, duration=5):
    length = len(text)
    delay = duration / length
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    passphrase = "SUpErSeCCuReKEyFoRMySeCRETMEssaGe!. "
    key = hashlib.sha256(passphrase.encode()).digest()  # 256-bit key

    encoded_string = input("Enter encoded encrypted message: ")
    encrypted_bytes = sixbit_string_to_bytes(encoded_string)

    decrypted_message = decrypt(encrypted_bytes, key)

    print("Decrypted message: ", end='', flush=True)
    slow_print(decrypted_message, duration=5)

if __name__ == "__main__":
    main()
