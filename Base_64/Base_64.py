import base64

hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Convert hex to bytes
bytes_data = bytes.fromhex(hex_string)

# Encode bytes to Base64
base64_data = base64.b64encode(bytes_data)

# Convert to string
flag = base64_data.decode('ascii')
print(flag)
