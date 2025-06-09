from Crypto.Hash import SHA3_256

# Function to calculate SHA3-256 hash
def sha3(message):
    sha3_hash = SHA3_256.new()  # Create a new SHA3-256 hash object
    sha3_hash.update(message)  # Update the hash object with the message
    return sha3_hash.digest()  # Return the digest (raw bytes)

# Main function
def main():
    text = input("Enter text string: ").encode('utf-8')  # Get the input and encode to bytes

    hashed_text = sha3(text)  # Calculate the SHA3-256 hash of the input text

    # Print the results
    print("Entered text string:", text.decode('utf-8'))  # Decode bytes back to string
    print("SHA-3 Hash:", hashed_text.hex())  # Print the hash in hexadecimal format

# Ensure the main function runs only when this script is executed directly
if __name__ == "__main__":
    main()
