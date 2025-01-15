from pwn import *

r= remote("ctf.mf.grsu.by", 9035)

print(r.recvuntil(b">").decode("utf-8"))
r.sendline(b"Lazarus")
print(r.recvuntil(b">").decode("utf-8"))
r.sendline(b"2009")
print(r.recvuntil(b">").decode("utf-8"))
r.sendline(b"Wiper")
print(r.recvuntil(b">").decode("utf-8"))
r.sendline(b"Sony")
print(r.recvuntil(b">").decode("utf-8"))
r.sendline(b"WannaCry")
print(r.recvuntil(b">").decode("utf-8"))
r.sendline(b"Eternal Blue")
print(r.recvuntil(b">").decode("utf-8"))
r.sendline(b"NSA")
print(r.recvall().decode("utf-8"))

r.close()
#grodno{1b6c8092cbb0546cb07395536c4e61dc73f0cf2}