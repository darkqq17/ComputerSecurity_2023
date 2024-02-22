from pwn import *

# nc chal1.eof.ais3.org 10002
if __name__ == '__main__':
    r = remote('chal1.eof.ais3.org', 10002)
    r.recvuntil('FLAG:  ')
    flag_1_bytes = r.recvline().strip()  # flag_1 is in bytes
    flag_1_str = flag_1_bytes.decode()  # decode bytes to string
    flag_1_num = int(flag_1_str)  # convert string to integer
    print("flag_1:", flag_1_num)
    r.sendlineafter('Any message for me?', str(flag_1_num))  # send as string
    r.recvuntil('New Message:  ')
    flag_2_bytes = r.recvline().strip()
    flag_2_str = flag_2_bytes.decode()  # decode bytes to string
    flag_2_num = int(flag_2_str)  # convert string to integer
    print("flag_2:", flag_2_num)
    r.sendlineafter('Any message for me?', str(flag_1_num))  # send as string
    r.recvuntil('New Message:  ')
    flag_3_bytes = r.recvline().strip()
    flag_3_str = flag_3_bytes.decode()  # decode bytes to string
    flag_3_num = int(flag_3_str)  # convert string to integer
    print("flag_3:", flag_3_num)
    r.interactive()
