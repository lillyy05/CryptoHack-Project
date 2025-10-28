import json    
import socket            

HOST = "socket.cryptohack.org"  
PORT = 13382                 

N_HEX = "FFFFFFFF00000000FFFFFFFFFFFFFFFFBCE6FAADA7179E84F3B9CAC2FC632551"  # prime hex
N = int(N_HEX, 16)            # prime int

private_key = N + 1           # private key (chosen)

bing_x = int("3B827FF5E8EA151E6E51F8D0ABF08D90F571914A595891F9998A5BD49DFA3531", 16)  # generator x
bing_y = int("AB61705C502CA0F7AA127DEC096B2BBDC9BD3B4281808B3740C320810888592A", 16)  # generator y

payload = {                   # JSON payload
    "private_key": private_key, 
    "host": "attacker.example", 
    "curve": "secp256r1", 
    "generator": [bing_x, bing_y],
}

def send_json(host, port, obj):
    with socket.create_connection((host, port)) as s:  # open TCP connection
        s.settimeout(10)                               # recv timeout
        banner = s.recv(4096).decode(errors="ignore")  # read banner
        print("Banner:", banner.strip())               # show banner
        
        data = (json.dumps(obj) + "\n").encode()       # serialize + newline
        s.sendall(data)                                # send payload
        
        chunks = []                                    # collect reply
        try:
            while True:
                part = s.recv(4096)                    # read part of response
                if not part:
                    break                              # connection closed
                chunks.append(part)                   
                if b"\n" in part or len(part) < 4096:
                    break                               # end of message 
        except socket.timeout:
            pass                                        # timeout -> stop
        return b"".join(chunks).decode(errors="ignore") # return response

if __name__ == "__main__":
    resp = send_json(HOST, PORT, payload)               # call function
    print("Response:", resp.strip())                    # print response

# This code connects to a remote server, sends it some cryptography-related data in JSON format, and waits for a reply. It basically tests how the server responds when given a specially chosen “private key” and curve information.
