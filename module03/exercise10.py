message1 = b"\xf0\x9d\x84\x9e"  # 𝄞
print(message1)
print(message1.decode("utf-8"))
message2 = "𝄞"
print(message2)
print(message2.encode("utf-8"))