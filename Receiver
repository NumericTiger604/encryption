import time

# Replace this with your real sensor reading function
def read_lux_sensor():
    # Your TSL559 reading code here
    # Example:
    # return sensor.lux
    return 1500  # placeholder for testing

lux_threshold = 1000
bit_period = 0.5

print("Receiver started. Waiting for messages...")

while True:
    bits_string = ""
    
    # --- Wait for start signal ---
    print("\nWaiting for start signal (light ON for 0.5s)...")
    while True:
        start_time = time.time()
        initial_state = read_lux_sensor() >= lux_threshold

        if initial_state:  # Light is ON
            # Check if ON for whole bit_period
            while time.time() - start_time < bit_period:
                current_state = read_lux_sensor() >= lux_threshold
                if not current_state:
                    break  # Light went OFF early, reset wait
                time.sleep(0.01)
            else:
                # Stable ON for 0.5s -> Start signal received
                print("Start signal detected! Beginning to read data bits...")
                break
        time.sleep(0.01)

    # --- Read data bits ---
    while True:
        start_time = time.time()
        initial_state = read_lux_sensor() >= lux_threshold

        # Wait for stable bit_period
        while time.time() - start_time < bit_period:
            current_state = read_lux_sensor() >= lux_threshold
            if current_state != initial_state:
                start_time = time.time()
                initial_state = current_state
            time.sleep(0.01)

        bit = '1' if initial_state else '0'
        bits_string += bit
        print(f"Collected bits so far: {bits_string}")

        if len(bits_string) >= 6 and bits_string[-6:] == "000000":
            print("\nEnd of transmission detected.")
            print(f"Final received bits: {bits_string}")
            break

    # --- DECODE YOUR MESSAGE HERE ---
    # For example, decode every 6 bits (excluding the last 6 zeros)
    data_bits = bits_string[:-6]  # remove the end code
    
    # Example: split into 6-bit chunks
    chunks = [data_bits[i:i+6] for i in range(0, len(data_bits), 6)]
    
    # Placeholder: just print the chunks for now
    print("Received chunks:")
    for c in chunks:
        print(c)
    
    # TODO: Add your custom decoding/uncryption logic here!
    # E.g., convert 6-bit chunks to characters or numbers
    
    print("\nReady to receive next message.")
