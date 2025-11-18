# ------------------------------------------
# Simplified DES Decryption with Reverse Keys
# ------------------------------------------

LEFT_SHIFTS = [1, 1, 2, 2, 2, 2, 2, 2,
               1, 2, 2, 2, 2, 2, 2, 1]

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def generate_subkeys(key56):
    """Generate 16 DES subkeys from 56-bit key."""
    C = key56[:28]
    D = key56[28:]
    subkeys = []

    for shift in LEFT_SHIFTS:
        C = left_shift(C, shift)
        D = left_shift(D, shift)
        subkeys.append(C + D)   # 56-bit → simplified

    return subkeys

def feistel(right, key):
    # simplified XOR-only Feistel function
    return ''.join('1' if right[i] != key[i] else '0' for i in range(len(right)))

def des_decrypt(cipher64, key56):
    subkeys = generate_subkeys(key56)  # normal schedule
    subkeys.reverse()                  # REVERSE for decryption

    L = cipher64[:32]
    R = cipher64[32:]

    for k in subkeys:
        newR = ''.join('1' if L[i] != feistel(R, k)[i] else '0' for i in range(32))
        L, R = R, newR

    return L + R


# ----------------------- MAIN --------------------------

cipher = input("Enter 64-bit ciphertext: ")
key = input("Enter 56-bit key: ")

plain = des_decrypt(cipher, key)

print("\nDecrypted plaintext (64 bits):")
print(plain)
