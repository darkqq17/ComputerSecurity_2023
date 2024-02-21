from pwn import *
from Crypto.Cipher import AES

def padding_oracle_attack(p, ct, iv):
    block_len = 16
    pt = b""
    # stop: -1. The loop will stop just before it hits this value. Thus, it won't actually reach -1.
    for i in range(block_len - 1, -1, -1):
        for c in range(1, 256):
            print(c)
            iv[i] ^= c
            p.sendline((iv + ct).hex().encode())
            ret = p.recvline()
            if ret == b"Well received :)\n":
                pt = bytes([c ^ 0x80]) + pt
                iv[i] ^= 0x80 #這裡要控制為 0x00(server padding方法不一樣)
                break
            else:
                iv[i] ^= c
        else:
            pt = bytes([0x80]) + pt
            iv[i] ^= 0x80
    
    return pt

p = remote('edu-ctf.zoolab.org', 10004)
output = bytes.fromhex(p.recvline(keepends=False).decode())
print("Output : ", output, "Output length:", len(output))

initialVector = output[:16]
print("InitialVector :", initialVector)
cipherText = output[16:]
print("CipherText :", cipherText)
plainText = b""

N = len(cipherText) // 16
# print(N)

for i in range(N):
    # print(cipherText[i * 16 : (i+1) * 16], "   ", bytearray(initialVector))
    plainText += padding_oracle_attack(p, cipherText[i * 16 : (i+1) * 16], bytearray(initialVector))
    print(plainText)
    initialVector = cipherText[i * 16 : (i+1) * 16]

print("PlainText :", plainText)