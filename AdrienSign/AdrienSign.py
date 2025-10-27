a = 288260533169915
p = 1007621497415251

# Read list from file
with open("output.txt") as f:
    ct = eval(f.read())

# Convert numbers to bits
bits = ''
for num in ct:
    if pow(num, (p-1)//2, p) == 1:
        bits += '1'
    else:
        bits += '0'

# Convert bits to text
flag = ''
for i in range(0, len(bits), 8):
    flag += chr(int(bits[i:i+8], 2))

print(flag)

