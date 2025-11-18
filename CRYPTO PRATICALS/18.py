# filename: 18_des_subkey_custom_split.py
"""
Construct 16 48-bit subkeys where first 24 bits come from subset A (28 bits)
and second 24 bits from subset B (disjoint 28 bits) of the initial 56-bit key.
This is a demonstrative key schedule, not real DES.
"""
import random

def bits_from_int(x, length):
    return [(x >> i) & 1 for i in range(length-1, -1, -1)]

def int_from_bits(bits):
    v = 0
    for b in bits:
        v = (v << 1) | (b & 1)
    return v

def make_subkeys(key56):
    # key56: integer 0..(1<<56)-1
    all_bits = bits_from_int(key56, 56)
    A = all_bits[:28]
    B = all_bits[28:]
    # for each round, rotate A and B by some schedule and pick top 24 bits each
    schedule = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]  # example left-rotations like DES
    subkeys = []
    a = A[:]
    b = B[:]
    for sh in schedule:
        # left rotate
        a = a[sh:] + a[:sh]
        b = b[sh:] + b[:sh]
        a24 = a[:24]
        b24 = b[:24]
        sub = a24 + b24  # 48 bits
        subkeys.append(int_from_bits(sub))
    return subkeys

def demo():
    k = random.getrandbits(56)
    subs = make_subkeys(k)
    for i,s in enumerate(subs,1):
        print(f"Round {i}: subkey (48-bit hex) = {s:012x}")

if __name__ == "__main__":
    demo()
