import hashlib

# Function to calculate the MD5 hash
def calculate_md5(input_string):
    md5_hash = hashlib.md5()  # Create a new MD5 hash object
    md5_hash.update(input_string.encode('utf-8'))  # Update the hash object with the input string (encoded in UTF-8)
    return md5_hash.hexdigest()  # Return the hexadecimal digest of the hash

# Prompt the user to enter a string
input_string = input("Enter string to hash: ")

# Calculate the MD5 hash of the input string
md5_hash = calculate_md5(input_string)

# Print the MD5 hash in hexadecimal format
print("The MD5 hash of string '{}' is: {}".format(input_string, md5_hash))
