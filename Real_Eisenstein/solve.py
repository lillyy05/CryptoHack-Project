import math
from decimal import *
getcontext().prec = 200  # use very high precision for math

# list of prime numbers
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]

# the encoded flag number trying to decode
ct = 1136269674509412708353842948972294549711695870304899125893388468609134417680692146

scale = Decimal(16**64)  # scale value for calculations
h_lower, h_upper = Decimal(ct) / scale, Decimal(ct + 1) / scale  # search range

# square root of each prime
prime_sqrt = [Decimal(p).sqrt() for p in PRIMES]

# add up the part already know: "crypto{" and "}"
known_sum = sum(ord("crypto{"[i]) * prime_sqrt[i] for i in range(7)) + ord("}") * prime_sqrt[-1]

# positions of letter don't know yet
unknown_indices = list(range(7, len(PRIMES) - 1))

def recover_flag(h_val):
    # guess the flag based on a possible hash value
    flag = list("crypto{" + "?" * len(unknown_indices) + "}")  # start with placeholders
    remaining = h_val - known_sum  # what’s left to match

    for pos in unknown_indices:
        # guess the character’s ASCII code
        char_code = int(round(float(remaining / prime_sqrt[pos])))
        # make sure it's a printable character
        flag[pos] = chr(max(32, min(126, char_code)))
        # remove this character's effect
        remaining -= ord(flag[pos]) * prime_sqrt[pos]

    return ''.join(flag)  # join into a string

def verify(flag):
    """check if the flag matches ct"""
    h = sum(ord(c) * prime_sqrt[i] for i, c in enumerate(flag))
    return math.floor(h * scale) == ct, math.floor(h * scale)

print(f"Target ct: {ct}\nSearching...")
best_flag, best_diff = None, None

# try 100,000 guesses between h_lower and h_upper (hash values)
for i in range(100000):
    h_test = h_lower + (h_upper - h_lower) * Decimal(i) / Decimal(99999)
    flag = recover_flag(h_test)
    match, ct_calc = verify(flag)

    if match:
        print(f"\n✓ Flag: {flag}")  # found the right flag
        break

    # check how close this guess is
    diff = abs(ct_calc - ct)
    if best_diff is None or diff < best_diff:
        best_diff, best_flag = diff, flag

    # show progress every 10,000 tries
    if i > 0 and i % 10000 == 0:
        print(f"  {i}/100000, best diff: {best_diff}")

# if no perfect match found, show closest one
if not match:
    print(f"\nBest: {best_flag} (diff: {best_diff})")

