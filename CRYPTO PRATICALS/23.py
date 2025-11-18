# filename: 23_counter_mode_demo.py
"""
Counter mode (CTR) using toy affine byte cipher (for demonstration).
Also shows how to implement CTR mode for any block cipher.
"""
def affine_enc_byte(m, a,b): return (a*m + b) % 256
def affine_dec_byte(c, a,b): return (pow(a,-1,256)*(c-b)) % 256

def ctr_encrypt_affine(plaintext, counter_start, a,b):
    ct = []
    counter = counter_start
    for p in plaintext:
        ks = affine_enc_byte(counter & 0xFF, a,b)
        ct.append(bytes([p ^ ks]))
        counter = (counter + 1) & 0xFF
    return b''.join(ct)

def ctr_decrypt_affine(ciphertext, counter_start, a,b):
    # symmetric
    return ctr_encrypt_affine(ciphertext, counter_start, a,b)

if __name__=='__main__':
    pt = bytes([0,1,2,3,4,5])
    ct = ctr_encrypt_affine(pt, 0, 5, 7)
    print("CTR ct:", ct)
    print("Recovered:", ctr_decrypt_affine(ct, 0, 5,7))
    print("\nFor S-DES CTR test vectors I can produce a full S-DES implementation on request.")
