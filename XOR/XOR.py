# The encrypted flag in hex
ciphertext_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

# Convert hex to bytes
ciphertext = bytes.fromhex(ciphertext_hex)

# The key discovered - "myXORkey"
key = b"myXORkey"

# XOR decrypt: plaintext = ciphertext XOR key
flag = bytes([ciphertext[i] ^ key[i % len(key)] for i in range(len(ciphertext))])

print(flag.decode())
