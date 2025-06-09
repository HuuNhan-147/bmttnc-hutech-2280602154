import hashlib

# Function to calculate the SHA-256 hash
def calculate_sha256_hash(data):
    sha256_hash = hashlib.sha256()  # Create a new SHA-256 hash object
    sha256_hash.update(data.encode('utf-8'))  # Update the hash object with the data (encoded to bytes)
    return sha256_hash.hexdigest()  # Return the hexadecimal representation of the hash

# Prompt the user to enter data to hash
data_to_hash = input("Enter data to hash using SHA-256: ")

# Calculate the SHA-256 hash of the input data
hash_value = calculate_sha256_hash(data_to_hash)

# Print the SHA-256 hash value
print("SHA-256 hash value:", hash_value)
