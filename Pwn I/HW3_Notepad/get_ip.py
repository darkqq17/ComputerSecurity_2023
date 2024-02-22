from pwn import *
import subprocess
r = remote('10.113.184.121', 10044)
r.recvuntil('sha256(')
pow_string = r.recvuntil(b" ")[:-1].decode()
print(pow_string)
result = subprocess.run(["python3", "pow_solver.py", pow_string, "22"], capture_output=True, text=True)
pow_solution = result.stdout.strip()
r.recvuntil('Answer: ')
r.sendline(pow_solution)
r.interactive()

