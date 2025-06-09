import base64

def main():
    # Prompt the user to enter a string for encoding
    input_string = input("Enter information to be encrypted: ")

    # Base64 encode the input string
    encoded_bytes = base64.b64encode(input_string.encode("utf-8"))
    
    # Decode the bytes to get the string representation
    encoded_string = encoded_bytes.decode("utf-8")

    # Write the encoded string to a file
    with open("data.txt", "w") as file:
        file.write(encoded_string)

    print("Encoded and written to data.txt file")

# Correct the typo in the if __name__ check
if __name__ == "__main__":
    main()
