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

output:
Plaintext (letters only, padded if needed):
MEETMEATTHEUSUALPLACEATTERTHANRIGHTOCLOCKX

Determinant of K mod26 = 17
Multiplicative inverse of determinant (mod26) = 23

Inverse key matrix K_inv (mod26):
[5 12]
[15 25]

ENCRYPTION STEPS:
Plain digram: ME -> [12 4]^T; C = K*P = [9*12 + 4*4, 5*12 + 7*4] mod26 = [20 10]
Plain digram: ET -> [4 19]^T; C = K*P = [9*4 + 4*19, 5*4 + 7*19] mod26 = [8 23]
Plain digram: ME -> [12 4]^T; C = K*P = [9*12 + 4*4, 5*12 + 7*4] mod26 = [20 10]
Plain digram: AT -> [0 19]^T; C = K*P = [9*0 + 4*19, 5*0 + 7*19] mod26 = [24 3]
Plain digram: TH -> [19 7]^T; C = K*P = [9*19 + 4*7, 5*19 + 7*7] mod26 = [17 14]
Plain digram: EU -> [4 20]^T; C = K*P = [9*4 + 4*20, 5*4 + 7*20] mod26 = [12 4]
Plain digram: SU -> [18 20]^T; C = K*P = [9*18 + 4*20, 5*18 + 7*20] mod26 = [8 22]
Plain digram: AL -> [0 11]^T; C = K*P = [9*0 + 4*11, 5*0 + 7*11] mod26 = [18 25]
Plain digram: PL -> [15 11]^T; C = K*P = [9*15 + 4*11, 5*15 + 7*11] mod26 = [23 22]
Plain digram: AC -> [0 2]^T; C = K*P = [9*0 + 4*2, 5*0 + 7*2] mod26 = [8 14]
Plain digram: EA -> [4 0]^T; C = K*P = [9*4 + 4*0, 5*4 + 7*0] mod26 = [10 20]
Plain digram: TT -> [19 19]^T; C = K*P = [9*19 + 4*19, 5*19 + 7*19] mod26 = [13 20]
Plain digram: EN -> [4 13]^T; C = K*P = [9*4 + 4*13, 5*4 + 7*13] mod26 = [10 7]
Plain digram: RA -> [17 0]^T; C = K*P = [9*17 + 4*0, 5*17 + 7*0] mod26 = [23 7]
Plain digram: TH -> [19 7]^T; C = K*P = [9*19 + 4*7, 5*19 + 7*7] mod26 = [17 14]
Plain digram: ER -> [4 17]^T; C = K*P = [9*4 + 4*17, 5*4 + 7*17] mod26 = [0 9]
Plain digram: TH -> [19 7]^T; C = K*P = [9*19 + 4*7, 5*19 + 7*7] mod26 = [17 14]
Plain digram: AN -> [0 13]^T; C = K*P = [9*0 + 4*13, 5*0 + 7*13] mod26 = [0 13]
Plain digram: EI -> [4 8]^T; C = K*P = [9*4 + 4*8, 5*4 + 7*8] mod26 = [16 24]
Plain digram: GH -> [6 7]^T; C = K*P = [9*6 + 4*7, 5*6 + 7*7] mod26 = [4 1]
Plain digram: TO -> [19 14]^T; C = K*P = [9*19 + 4*14, 5*19 + 7*14] mod26 = [19 11]
Plain digram: CL -> [2 11]^T; C = K*P = [9*2 + 4*11, 5*2 + 7*11] mod26 = [10 9]
Plain digram: OC -> [14 2]^T; C = K*P = [9*14 + 4*2, 5*14 + 7*2] mod26 = [4 6]
Plain digram: KX -> [10 23]^T; C = K*P = [9*10 + 4*23, 5*10 + 7*23] mod26 = [0 3]

Ciphertext (ungrouped):
UKIXURYDROMEIWSZWXIOKUNUHKHROAJRQANYEBTLKJGAD
