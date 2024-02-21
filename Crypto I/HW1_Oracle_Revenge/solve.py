from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Cipher import AES
from pwn import *

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
        # print(result_list)
    return bytes_to_long(bytes(result_list))

# Decrypt when we get key and iv
def symmetric_decryption(message, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(message))
    return pt

if __name__ == '__main__':
    r = remote('10.113.184.121', 10031)
    N = 69214008498642035761243756357619851816607540327248468473247478342523127723748756926949706235406640562827724567100157104972969498385528097714986614165867074449238186426536742677816881849038677123630836686152379963670139334109846133566156815333584764063197379180877984670843831985941733688575703811651087495223
    e = 65537
    ans = bytearray(b'\x00' * 128)
    aes_key = b'1234567890123456'
    
    plaintext_template_iv = bytearray(b'\x00' * 16)
    encrypted_flag = 67448907891721241368838325896320122397092733550961191069708016032244349188684070793897519352151466622385197077064799553157879456334546372809948272281247935498288157941438709402245513879910090372080411345199729220479271018326225319584057160895804120944126979515126944833368164622466123481816185794224793277249
    
    mod = 2 ** 128
    mod_inv = pow(mod, -1, N)
    mod_inv_e = pow(mod, -e, N)
    ans = 0
    counter = 1
    remainder = 0

    while counter <= N:
        # print(counter)
        tmp = find_value(plaintext_template_iv, encrypted_flag, padding_oracle, N, e)
        x = (tmp - remainder) % mod
        ans += x * counter
        
        encrypted_flag = (encrypted_flag * mod_inv_e) % N
        remainder = (remainder + x) * mod_inv % N
        counter *= mod
        
    print(long_to_bytes(ans))
