from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Cipher import AES
from pwn import *

# Sample code
def pad(m):
    length = 16 - len(m) % 16
    return m + chr(length).encode() * length

def unpad(c):
    length = c[-1]
    for char in c[-length:]:
        if char != length:
            raise ValueError
    return c[:-length]

# My AES encryption, iv needs to be all zero!
def symmetric_encryption(message, key):
    iv = b'\x00' * 16
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct = cipher.encrypt(message)
    return ct

def rsa_encryption(message, N, e):
    message_int = bytes_to_long(message)
    encrypted_int = pow(message_int, e, N)
    return encrypted_int

def padding_oracle(encrypted_key, encrypted_iv, ct):
    r.recvuntil("Give me the encrypted key: ")
    r.sendline(encrypted_key)
    r.recvuntil("Give me the encrypted iv: ")
    r.sendline(encrypted_iv)
    r.recvuntil("Give me the ciphertext: ")
    r.sendline(ct)
    return r.recvline()

def find_byte(plaintext, encrypted_target, index, padding_oracle, N, e):
    for i in range(256):
        modified_plaintext = bytearray(plaintext)
        modified_plaintext[index] ^= i
        ct = symmetric_encryption(modified_plaintext, aes_key)
        rsa_aes_key = rsa_encryption(aes_key, N, e)
        response = padding_oracle(str(rsa_aes_key), str(encrypted_target), str(ct.hex()))
        if response == b'OK! Got it.\n':
            return modified_plaintext
    raise ValueError("Error, didn't return byte value")

def find_value(plaintext_template, encrypted_target, padding_oracle, N, e):
    result_list = bytearray(b'\x00' * 16)
    for index in range(15, -1, -1):
        for i in range(15, index, -1):
            plaintext_template[i] = result_list[i] ^ (16 - index)
        target_byte = find_byte(plaintext_template, encrypted_target, index, padding_oracle, N, e)
        result_list[index] = target_byte[index] ^ (16 - index)
        print(result_list)
    return result_list

# Decrypt when we get key and iv
def symmetric_decryption(message, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(message))
    return pt

if __name__ == '__main__':
    r = remote('10.113.184.121', 10031)
    N = 69214008498642035761243756357619851816607540327248468473247478342523127723748756926949706235406640562827724567100157104972969498385528097714986614165867074449238186426536742677816881849038677123630836686152379963670139334109846133566156815333584764063197379180877984670843831985941733688575703811651087495223
    e = 65537

    # My own plaintext & key & IV
    aes_key = b'1357926145486231'
    plaintext_template_iv = bytearray(b'\x00' * 16)
    plaintext_template_key = bytearray(b'\x00' * 16)
    encrypted_iv = 35154524936059729204581782839781987236407179504895959653768093617367549802652967862418906182387861924584809825831862791349195432705129622783580000716829283234184762744224095175044663151370869751957952842383581513986293064879608592662677541628813345923397286253057417592725291925603753086190402107943880261658
    encrypted_key = 65690013242775728459842109842683020587149462096059598501313133592635945234121561534622365974927219223034823754673718159579772056712404749324225325531206903216411508240699572153162745754564955215041783396329242482406426376133687186983187563217156659178000486342335478915053049498619169740534463504372971359692

    iv_list = find_value(plaintext_template_iv, encrypted_iv, padding_oracle, N, e)
    key_list = find_value(plaintext_template_key, encrypted_key, padding_oracle, N, e)

    print("IV:", iv_list)
    print("Key:", key_list)
    
    cypher_text = open("encrypted_flag.not_png", "rb").read()
    pt = symmetric_decryption(cypher_text, bytes(key_list), bytes(iv_list))
    with open("FLAG.png", "wb") as f:
        f.write(pt)
        



# def find_byte(plaintext, encrypted_target, index, padding_oracle, N, e):
#     """
#     Find a byte of the plaintext by exploiting the padding oracle.
#     """
#     modified_plaintext = bytearray(plaintext)
    
#     for potential_byte in range(256):
#         modified_plaintext[index] ^= potential_byte
#         ct = symmetric_encryption(modified_plaintext, aes_key)
#         rsa_aes_key = rsa_encryption(aes_key, N, e)
        
#         response = padding_oracle(str(rsa_aes_key), str(encrypted_target), str(ct.hex()))
#         if response == b'OK! Got it.\n':
#             return modified_plaintext
        
#     raise ValueError("Couldn't determine byte value")

# def find_value(plaintext_template, encrypted_target, padding_oracle, N, e):
#     """
#     Find the entire block of plaintext.
#     """
#     result_list = bytearray(b'\x00' * 16)
#     for index in reversed(range(16)):
#         for i in range(15, index, -1):
#             plaintext_template[i] = result_list[i] ^ (16 - index)
        
#         modified_byte = find_byte(plaintext_template, encrypted_target, index, padding_oracle, N, e)
#         result_list[index] = modified_byte[index] ^ (16 - index)
#         print(result_list)
        
#     return result_list