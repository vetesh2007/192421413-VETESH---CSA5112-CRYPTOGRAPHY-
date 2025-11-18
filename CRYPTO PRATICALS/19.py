# filename: 19_cbc_3des_choice.py
"""
Encrypt/decrypt using 3DES in CBC mode. Requires pycryptodome: pip install pycryptodome
Also prints an opinion: 3DES vs DES for security and performance.
"""
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

def pad8(b): return b + b'\x00' * ((8 - len(b) % 8) % 8)

key = DES3.adjust_key_parity(get_random_bytes(24))  # 24-byte 3DES key
iv = get_random_bytes(8)
cipher = DES3.new(key, DES3.MODE_CBC, iv)
pt = b"Confidential message that will be encrypted with 3DES"
ct = cipher.encrypt(pad8(pt))
print("3DES-CBC ciphertext (hex):", ct.hex())

dec = DES3.new(key, DES3.MODE_CBC, iv)
print("Decrypted:", dec.decrypt(ct).rstrip(b'\x00'))

print("\nChoice:")
print("a) For security? 3DES is much stronger than single DES (DES is insecure). Choose 3DES (or better AES).")
print("b) For performance? DES is faster (single DES) but insecure; 3DES is slower due to multiple DES ops. For performance+security choose AES.")
