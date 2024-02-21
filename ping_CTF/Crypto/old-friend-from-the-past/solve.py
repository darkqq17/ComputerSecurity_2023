file_path = 'encrypted_data.bin'

def decrypt_caesar_ascii_pro_bytes(encrypted_bytes, shift=79):
    decrypted_bytes = bytearray()

    for encrypted_byte in encrypted_bytes:
        decrypted_byte = (encrypted_byte + shift) % 256
        decrypted_bytes.append(decrypted_byte)

    return bytes(decrypted_bytes)

def ascii_array_to_text(ascii_array):
    text = ''.join([chr(ascii_value) for ascii_value in ascii_array])
    return text

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

# Read encrypted bytes from the binary file
with open(file_path, 'rb') as file:
        read_encrypted_bytes = file.read()
# Decrypt the encrypted bytes
print(f"Encrypted bytes : {read_encrypted_bytes}")

decrypted_bytes = decrypt_caesar_ascii_pro_bytes(read_encrypted_bytes)
print(f"Decrypted bytes : {decrypted_bytes}")

# Convert decrypted ASCII array to text
decrypted_text = ascii_array_to_text(decrypted_bytes)
# Decrypt the text using a Caesar cipher
decrypted_text = caesar_cipher(decrypted_text, -9)
print(f"Decrypted text : {decrypted_text}")