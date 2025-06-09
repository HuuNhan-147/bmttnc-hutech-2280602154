import hashlib

# Function to calculate BLAKE2b hash (with 64-byte output)
def blake2(message):
    blake2_hash = hashlib.blake2b(digest_size=64)  # Create a new BLAKE2b hash object with 64-byte output
    blake2_hash.update(message)  # Update the hash object with the message
    return blake2_hash.digest()  # Return the digest (raw bytes)

# Main function
def main():
    text = input("Enter text string: ").encode('utf-8')  # Get the input and encode it as bytes

    hashed_text = blake2(text)  # Calculate the BLAKE2b hash of the input text

    # Print the results
    print("Entered text string:", text.decode('utf-8'))  # Decode bytes back to string
    print("BLAKE2 Hash:", hashed_text.hex())  # Print the hash in hexadecimal format

# Ensure the main function runs only when this script is executed directly
if __name__ == "__main__":
    main()
