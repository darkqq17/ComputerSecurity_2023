import re
from base64 import b64encode, b64decode
from Crypto.Util.number import long_to_bytes as l2b, bytes_to_long as b2l
from pwn import remote

def XOR (a, b):
    return l2b(b2l(a) ^ b2l(b)).rjust(len(a), b"\x00")

def send_encryption_request(r, mode, pt):
    r.sendlineafter(b"What operation mode do you want for encryption? ", mode.encode())
    r.sendlineafter(b"What message do you want to encrypt (in base64)? ", b64encode(pt))
    return recv_bytes(r)

def recv_cipher(r):
    text = r.recvuntil(b'\')')
    matches = re.findall(r"b'([^']+)'", text.decode())
    return [b64decode(bytes(match, 'utf-8')) for match in matches]

def recv_bytes(r):
    text = r.recvline()
    matches = re.findall(r"b'([^']+)'", text.decode())
    return b64decode(bytes(matches[1], 'utf-8'))

def main():
    r = remote('chal1.eof.ais3.org', 10003)
    
    BLOCK_SIZE = 16  # AES block size in bytes
    zeros = b'\x00' * BLOCK_SIZE
    counter_0, enc_c1 = recv_cipher(r)
    print(f'counter_0: {counter_0}', f'enc_c1: {enc_c1}')
    counter_1, enc_c2 = recv_cipher(r)
    print(f'counter_1: {counter_1}', f'enc_c2: {enc_c2}')
    counter_2, enc_c3 = recv_cipher(r)
    print(f'counter_2: {counter_2}', f'enc_c3: {enc_c3}')

    # Encrypting zeros with CTR mode to get counters encryption
    counters_enc = send_encryption_request(r, 'CTR', zeros * 5)
    print(f'counters_enc: {counters_enc}')
    
    # Decrypting c1
    res1 = send_encryption_request(r, 'CFB', XOR(counter_0, counters_enc[16:32]) + zeros)
    c1 = XOR(enc_c1[0:16], res1[16:32])
    res2 = send_encryption_request(r, 'CFB', XOR(enc_c1[:16], counters_enc[32:48]) + zeros)
    c1 += XOR(enc_c1[16:32], res2[16:32])

    # Decrypting c2
    res3 = send_encryption_request(r, 'CFB', XOR(counter_1, counters_enc[48:64]) + zeros * 2)
    c2 = XOR(enc_c2[0:16], res3[16:32])
    c2 += XOR(enc_c2[16:32], res3[32:48])

    # Decrypting c3
    res4 = send_encryption_request(r, 'CFB', XOR(counter_2, counters_enc[64:80]) + zeros)
    c3 = XOR(enc_c3[0:16], res4[16:32])
    c3 += XOR(enc_c3[16:32], counters_enc[0:16])

    # Combining decrypted data to get the flag
    flag = XOR(XOR(c1, c2), c3)
    print(f'Flag: {flag}')

if __name__ == "__main__":
    main()
