import RPi.GPIO as GPIO
import time

# === GPIO Setup ===
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

OUTPUT_PIN = 22
GPIO.setup(OUTPUT_PIN, GPIO.OUT)
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!,.?-=+/%^ "

# === Helper Functions ===

def len5(awacky):
    """Ensure binary string is 6 bits long."""
    while len(awacky) < 6:
        awacky = "0" + awacky
    return awacky

def flash():
    """Flash LED to represent a binary '1'."""
    GPIO.output(OUTPUT_PIN, GPIO.HIGH)
    print(1)
    time.sleep(0.5)

def flashing(inputs):
    """Flash LED according to binary string."""
    for bit in inputs:
        if bit == "0":
            print(0)
            GPIO.output(OUTPUT_PIN, GPIO.LOW)
            time.sleep(0.5)
        else:
            flash()
    return True

# === MAIN CODE ===

message = input("Enter message to send: ")

wackyBinary = "1"  # Starting dummy bit for formatting

# Convert each character to 6-bit binary representation
for char in message:
    lPos = letters.find(char)
    if lPos == -1:
        print(f"Warning: Character '{char}' not in alphabet. Skipping.")
        continue
    binary = bin(lPos)[2:]        # Remove '0b'
    padded = len5(binary)         # Pad to 6 bits
    wackyBinary += padded + " "

wackyBinary = wackyBinary.strip()  # Remove initial dummy bit
binaryArray = wackyBinary[1:].split(" ")   # Split into 6-bit chunks

print("Binary for transmission:")
print(wackyBinary)

flashing(wackyBinary)

# Decode binary to verify transmitted string
print("Decoded (reconstructed) characters from binary:")
for bit in binaryArray:
    number = int(bit, 2)
    character = letters[number]
    print(character, end="")
print()
GPIO.output(OUTPUT_PIN, GPIO.LOW)
