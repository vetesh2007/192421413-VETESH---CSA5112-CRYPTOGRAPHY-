# hill_2x2.py
# 2x2 Hill cipher encrypt/decrypt with detailed steps for key [[9,4],[5,7]]

import math

def mod26(x):
    return x % 26

def egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None
    return x % m

def process_text(s):
    s = ''.join(ch for ch in s.upper() if ch.isalpha())
    if len(s) % 2 == 1:
        s += 'X'
    return s

def encrypt(plain, K):
    cipher = []
    print("ENCRYPTION STEPS:")
    for i in range(0, len(plain), 2):
        a = ord(plain[i]) - 65
        b = ord(plain[i+1]) - 65
        c1 = mod26(K[0][0]*a + K[0][1]*b)
        c2 = mod26(K[1][0]*a + K[1][1]*b)
        print(f"Plain digram: {plain[i]}{plain[i+1]} -> [{a:2d} {b:2d}]^T ; "
              f"C = K*P = [{K[0][0]}*{a} + {K[0][1]}*{b} , {K[1][0]}*{a} + {K[1][1]}*{b}] mod26 = [{c1:2d} {c2:2d}]")
        cipher.append(chr(c1 + 65))
        cipher.append(chr(c2 + 65))
    return ''.join(cipher)

def decrypt(cipher, invK):
    plain = []
    print("DECRYPTION STEPS:")
    for i in range(0, len(cipher), 2):
        a = ord(cipher[i]) - 65
        b = ord(cipher[i+1]) - 65
        p1 = mod26(invK[0][0]*a + invK[0][1]*b)
        p2 = mod26(invK[1][0]*a + invK[1][1]*b)
        print(f"Cipher digram: {cipher[i]}{cipher[i+1]} -> [{a:2d} {b:2d}]^T ; "
              f"P = K_inv*C = [{invK[0][0]}*{a} + {invK[0][1]}*{b} , {invK[1][0]}*{a} + {invK[1][1]}*{b}] mod26 = [{p1:2d} {p2:2d}]")
        plain.append(chr(p1 + 65))
        plain.append(chr(p2 + 65))
    return ''.join(plain)

if __name__ == "__main__":
    raw = "meet me at the usual place at ten rather than eight oclock"
    clean = process_text(raw)
    print("Processed plaintext (letters only, padded if needed):")
    print(clean)
    print()

    K = [[9,4],[5,7]]
    # determinant
    det = mod26(K[0][0]*K[1][1] - K[0][1]*K[1][0])
    print(f"Determinant of K mod26 = {det}")
    det_inv = modinv(det, 26)
    if det_inv is None:
        raise SystemExit("Key matrix not invertible mod 26.")
    print(f"Multiplicative inverse of determinant (mod26) = {det_inv}\n")

    # inverse matrix
    invK = [
        [mod26(det_inv * K[1][1]), mod26(-det_inv * K[0][1])],
        [mod26(-det_inv * K[1][0]), mod26(det_inv * K[0][0])]
    ]
    print("Inverse key matrix K_inv (mod26):")
    print(f"[{invK[0][0]} {invK[0][1]}]")
    print(f"[{invK[1][0]} {invK[1][1]}]\n")

    cipher = encrypt(clean, K)
    print("\nCiphertext (ungrouped):")
    print(cipher)
    print()
    decrypted = decrypt(cipher, invK)
    print("\nDecrypted text (should match cleaned plaintext):")
    print(decrypted)
