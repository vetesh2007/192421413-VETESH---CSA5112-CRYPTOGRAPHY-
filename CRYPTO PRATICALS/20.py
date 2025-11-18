# filename: 20_ecb_cbc_error_demo.py
"""
Demonstrate error propagation: ECB vs CBC.
Uses a toy block cipher (XOR with key) for clarity, not secure.
"""
def xor(a,b): return bytes(x^y for x,y in zip(a,b))

def toy_encrypt_block(key, block):
    return xor(block, key)  # NOT secure; just for propagation demonstration

def ecb_encrypt(blocks, key):
    return [toy_encrypt_block(key, b) for b in blocks]

def cbc_encrypt(blocks, key, iv):
    cprev = iv
    cblocks=[]
    for p in blocks:
        c = toy_encrypt_block(key, xor(p, cprev))
        cblocks.append(c); cprev = c
    return cblocks

# Demo:
bs = 8
blocks = [bytes([i]*bs) for i in range(1,6)]  # P1..P5
key = bytes([0xAA]*bs)
iv = bytes([0]*bs)

ecb_ct = ecb_encrypt(blocks, key)
cbc_ct = cbc_encrypt(blocks, key, iv)

# Simulate single-bit corruption in transmitted C1:
def flip_bit(b):
    lst = list(b)
    lst[0] ^= 0x01
    return bytes(lst)

cbc_ct_corrupt = cbc_ct[:]
cbc_ct_corrupt[0] = flip_bit(cbc_ct_corrupt[0])
# Decrypt toy CBC (reverse)
def cbc_decrypt(cblocks, key, iv):
    prev = iv; plains=[]
    for c in cblocks:
        p = xor(toy_encrypt_block(key, c), prev)
        plains.append(p)
        prev = c
    return plains

plain_corrupted = cbc_decrypt(cbc_ct_corrupt, key, iv)

print("If transmitted C1 corrupted -> receiver sees P1 and P2 corrupted; beyond P2 unaffected.")
print("If original P1 had a bit error BEFORE encryption -> affects C1 and thus all subsequent ciphertexts; receiver sees corruption from P1 onward.")
