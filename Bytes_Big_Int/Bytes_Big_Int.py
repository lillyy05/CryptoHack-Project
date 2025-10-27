big_number = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

# Convert to hex (removes '0x' prefix) 
hex_string = hex(big_number)[2:]

# Convert hex to bytes
bytes_data = bytes.fromhex(hex_string)

# Convert bytes to string
flag = bytes_data.decode('ascii')

print(flag)

# The 0x prefix tells that a number is hexadecimal however, hex digits represent the value.