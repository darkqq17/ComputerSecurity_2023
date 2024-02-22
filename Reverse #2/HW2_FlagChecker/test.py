# Initial hexadecimal key
v3 = 0xE0C92EAB

# Array of hexadecimal values for processing
v8 = [
    0xED, 0x03, 0x81, 0x69,
    0x7B, 0x84, 0xA6, 0xA0,
    0x5B, 0x2B, 0xB6, 0xE6,   
    0x5C, 0x57, 0xC9, 0x99,
    0xE8, 0xB2, 0x20, 0x72,
    0x38, 0xF1, 0x58
]

def rotate_bits_right(number, shift):
    """
    Perform a right bit rotation on a 32-bit integer.
    """
    return (number >> shift) | ((number << (32 - shift)) & 0xFFFFFFFF)

def calculate_sequence(start_value):
    """
    Generate a sequence of values based on the start value and v8 array.
    """
    current_value, sequence = start_value, [start_value]
    # print(current_value, sequence)
    for index, value in enumerate(v8):
        # print(index, value)
        current_value = (rotate_bits_right(current_value, 3) ^ value) + len(v8) - index
        sequence.append(current_value)
        # print(sequence)
    return sequence

# Generate the sequence based on the initial key
value_sequence = calculate_sequence(v3)
# print(value_sequence)

# Decoding the message
decoded_message = ''
for i in range(len(v8)):
    # print(value_sequence[i], v8[i], value_sequence[i] ^ v8[i], (value_sequence[i] ^ v8[i]) & 0xFF)
    decoded_message += chr((value_sequence[i] ^ v8[i]) & 0xFF)
print(decoded_message)
