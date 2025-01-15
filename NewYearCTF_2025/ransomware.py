from pwn import *

r= remote("ctf.mf.grsu.by", 9037)

print(r.recvuntil(b">").decode("utf-8"))
r.sendline(b"EternalBlue")
print(r.recvuntil(b">").decode("utf-8"))
r.sendline(b"CVE-2017-0144")
print(r.recvuntil(b">").decode("utf-8"))
r.sendline(b"T1210")
print(r.recvuntil(b">").decode("utf-8"))
r.sendline(b"Lateral Movement")
print(r.recvuntil(b">").decode("utf-8"))
r.sendline(b"WannaCry")
print(r.recvuntil(b">").decode("utf-8"))
r.sendline(b"2017")
print(r.recvuntil(b">").decode("utf-8"))
r.sendline(b"Shadow Brokers")
print(r.recvuntil(b">").decode("utf-8"))
r.sendline(b"NSA")
print(r.recvuntil(b">").decode("utf-8"))
r.sendline(b"MS17-010")
print(r.recvall().decode())

r.close()

#grodno{1b60d01a1d3d373b95f085387f4cb0}