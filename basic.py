import socket
import time
import os
import struct
import telnetlib
import sys
import struct
import subprocess



def connecr(ip, port):
  return socket.create_connection((ip, port))
  
def p32(x):
  return struct.pack('<I',x)
  
def u32(x):
  return struct,unpack('<I', x)[0]
  
def interact(s):
  print('----- interactive mode -----')
  t = telnetlib.Telnet()
  t.sock = s
  t.interact()
  
s = connect(127.0.0.1',4000)

interact(s)
def interact(s):
