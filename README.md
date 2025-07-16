# encyption
an encryption for python 
# Encryption & Decryption Scripts

This project contains two Python scripts:

- `encrypt.py` — Encrypts a plaintext message and outputs a safe encoded string.
- `decrypt.py` — Decodes the encoded string and decrypts the message back to plaintext.

---

## Features

- Uses AES-GCM 256-bit encryption (secure and modern).
- Encodes encrypted bytes into a readable string using a custom 6-bit encoding.
- Easy to use on any machine with Python 3 and the `cryptography` package installed.
- Compatible with Raspberry Pi and IDEs like Thonny.

---

## Requirements

- Python 3.6 or higher
- [`cryptography`](https://cryptography.io/en/latest/) Python package

---

## Setup

1. **Install Python 3** (should already be on Raspberry Pi or most systems).

2. **Install the cryptography package:**

```bash
pip3 install cryptography
Download the scripts (encrypt.py and decrypt.py) to your device.

Usage
Encrypt a message:
Run the encrypt.py script:

bash
Copy
Edit
python3 encrypt.py
Enter the message you want to encrypt when prompted.

The script will output an encoded string representing the encrypted message.

Save this encoded string for transmission or storage.

Decrypt a message:
Run the decrypt.py script:

bash
Copy
Edit
python3 decrypt.py
Paste the encoded string when prompted.

The script will decode and decrypt the message, then slowly print the original plaintext.

Notes
The key is hardcoded and consistent between encrypt and decrypt scripts.

The encoded string uses letters (A-Z, a-z), digits (0-9), period (.), and space.

Make sure to keep the encoded string intact for successful decryption.

These scripts are great for learning and small projects but for real-world security, key management must be improved.

Running on Raspberry Pi
Open Thonny IDE.

Open the scripts and run as described above.

Make sure you have internet access for installing cryptography.
