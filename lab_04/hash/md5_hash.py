def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def md5(message):
    # Initialize the initial variables (MD5 constants)
    a = 0x67452301
    b = 0xEFCDAB89
    c = 0x98BADCFE
    d = 0x10325476

    # Preprocess the input message
    original_length = len(message)
    message += b'\x80'  # Append a single 1 bit (0x80)
    
    # Pad with zeroes to make the length a multiple of 64 (mod 512)
    while len(message) % 64 != 56:
        message += b'\x00'

    # Append the length of the original message as a 64-bit integer
    message += original_length.to_bytes(8, 'little')

    # Split the message into 512-bit (64-byte) blocks
    for i in range(0, len(message), 64):
        block = message[i:i+64]
        
        # Convert the block into 16 32-bit words
        words = [int.from_bytes(block[j:j+4], 'little') for j in range(0, 64, 4)]

        # Save the original values of a, b, c, d
        original_a, original_b, original_c, original_d = a, b, c, d

        # Main loop of MD5 algorithm
        for j in range(64):
            if j < 16:
                f = (b & c) | (~b & d)
                g = j
            elif j < 32:
                f = (d & b) | (~d & c)
                g = (5 * j + 1) % 16
            elif j < 48:
                f = b ^ c ^ d
                g = (3 * j + 5) % 16
            else:
                f = c ^ (b | ~d)
                g = (7 * j) % 16

            # Perform the main calculation
            temp = d
            d = c
            c = b
            b = (b + left_rotate((a + f + 0x5A827999 + words[g]) & 0xFFFFFFFF, 3)) & 0xFFFFFFFF
            a = temp

        # Update the hash values with the result of this block
        a = (a + original_a) & 0xFFFFFFFF
        b = (b + original_b) & 0xFFFFFFFF
        c = (c + original_c) & 0xFFFFFFFF
        d = (d + original_d) & 0xFFFFFFFF

    # Return the final hash value as a hexadecimal string
    return '{:08x}{:08x}{:08x}{:08x}'.format(a, b, c, d)

# Input from the user
input_string = input("Enter string to hash: ")

# Calculate the MD5 hash
md5_hash = md5(input_string.encode('utf-8'))

# Print the result
print(f"The MD5 hash of string '{input_string}' is: {md5_hash}")
