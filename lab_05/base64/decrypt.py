import base64

def main():
    try:
        # Open the file and read the encoded string
        with open("data.txt", "r") as file:
            encoded_string = file.read().strip()

        # Base64 decode the encoded string
        decoded_bytes = base64.b64decode(encoded_string)

        # Decode the bytes to a string
        decoded_string = decoded_bytes.decode("utf-8")

        print("String after decoding:", decoded_string)

    except Exception as e:
        print("Error:", e)

# Corrected the typo in the if __name__ check
if __name__ == "__main__":
    main()
