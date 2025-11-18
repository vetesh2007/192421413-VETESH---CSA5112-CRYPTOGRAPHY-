# filename: 30_cbc_mac_oneblock_forgery.py
"""
Demonstrate CBC-MAC forgery: for one-block message X with tag T = MAC(K,X),
the MAC for X || (X xor T) is also T.
Uses AES-ECB as the block cipher (pycryptodome) if available; else toy inversion.
"""
try:
    from Crypto.Cipher import AES
    HAVE_CRYPTO = True
except:
    HAVE_CRYPTO = False

def block_cipher_encrypt(key, block):
    if HAVE_CRYPTO:
        cipher = AES.new(key, AES.MODE_ECB)
        return cipher.encrypt(block)
    else:
        return bytes((~b)&0xFF for b in block)

def cbc_mac_tag(key, block):
    return block_cipher_encrypt(key, block)

def craft_forgery(X, key):
    T = cbc_mac_tag(key, X)
    forged = X + bytes(x^y for x,y in zip(X, T))
    return T, forged

if __name__=='__main__':
    key = (b'\x01'*16)
    X = b'HELLOWORLD12345'  # 16 bytes
    T, forged = craft_forgery(X, key)
    print("X:", X)
    print("T (hex):", T.hex())
    print("Forged message (hex):", forged.hex())
    print("Receiver will compute MAC(forged) == T (for single-block CBC-MAC).")
