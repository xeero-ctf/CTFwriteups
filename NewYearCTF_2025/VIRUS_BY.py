from pwn import *


for j in range(5):
    for i in range(5):
        r= remote("ctf.mf.grsu.by", 9033)
        print(r.recvuntil(b">").decode("utf-8"))
        r.sendline(b"neshta")
        print(r.recvuntil(b">").decode("utf-8"))
        r.sendline(b"something")
        print(r.recvuntil(b">").decode("utf-8"))
        r.sendline(b"2005")
        print(r.recvuntil(b">").decode("utf-8"))
        r.sendline(b"Delphi")
        print(r.recvuntil(b">").decode("utf-8"))
        r.sendline(b"Belarus")
        print(r.recvuntil(b">").decode("utf-8"))
        r.sendline(b"Dziadulja Apanas")
        print(r.recvuntil(b">").decode("utf-8"))
        r.sendline(b"Alivaria")
        print(r.recvuntil(b">").decode("utf-8"))
        r.sendline(b"svchost.com")
        print(r.recvuntil(b">").decode("utf-8"))
        r.sendline(b"Lukashenko")
        print(r.recvuntil(b">").decode("utf-8"))
        r.sendline(f"{i}:{j}")
        resp=r.recvall().decode("utf-8")
        if "grodno" in resp:
            break
        r.close()

#grodno{db9ee02312fe3ba5890a8f1cb9}

