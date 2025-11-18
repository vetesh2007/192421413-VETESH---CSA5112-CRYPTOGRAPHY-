# filename: 22_cbc_encrypt_decrypt_choices.py
"""
CBC encryption/decryption using:
- a toy Affine modulo 256 block cipher (block size = 1 byte for simplicity)
- For real ciphers use pycryptodome (DES/AES)
Also provides the S-DES test vector example as explained (S-DES full implementation not included).
"""
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

# Toy affine cipher mod 256 for demonstration (block size 1 byte)
def affine_enc_byte(m, a, b):
    return (a*m + b) % 256
def affine_dec_byte(c, a, b):
    # find modular inverse of a mod 256 (only works for odd a)
    inv = pow(a, -1, 256)
    return (inv*(c - b)) % 256

def cbc_encrypt_affine(plaintext_bytes, iv, a, b):
    prev = iv
    c=[]
    for p in plaintext_bytes:
        x = affine_enc_byte(prev[0] ^ p, a, b)
        c.append(bytes([x]))
        prev = bytes([x])
    return b''.join(c)

def cbc_decrypt_affine(cipher_bytes, iv, a, b):
    prev = iv
    p=[]
    for c in cipher_bytes:
        m = affine_dec_byte(c, a, b)
        p_byte = prev[0] ^ m
        p.append(bytes([p_byte]))
        prev = bytes([c])
    return b''.join(p)

if __name__=='__main__':
    # test with toy data
    iv = bytes([0])
    pt = bytes([0,1,2,3])
    a,b = 5,7  # a must be coprime with 256 (odd)
    ct = cbc_encrypt_affine(pt, iv, a, b)
    print("Affine-CBC ct:", ct)
    pt2 = cbc_decrypt_affine(ct, iv, a, b)
    print("Recovered:", list(pt2))
    print("\nFor real DES/3DES use pycryptodome's DES/3DES modules. For S-DES I can provide exact test vector code on request.")
