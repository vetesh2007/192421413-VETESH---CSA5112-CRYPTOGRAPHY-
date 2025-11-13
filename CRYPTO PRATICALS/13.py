# hill_known_plain.py
# Recover 2x2 Hill key given two plaintext-ciphertext digram pairs.

def mod26(x): return x % 26

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

def matrix_inverse_2x2(mat):
    a, b = mat[0]
    c, d = mat[1]
    det = mod26(a*d - b*c)
    det_inv = modinv(det, 26)
    if det_inv is None:
        return None
    inv = [
        [mod26(det_inv * d), mod26(-det_inv * b)],
        [mod26(-det_inv * c), mod26(det_inv * a)]
    ]
    return inv

def mat_mult_2x2(A, B):
    # multiply 2x2 matrices mod26
    return [
        [mod26(A[0][0]*B[0][0] + A[0][1]*B[1][0]), mod26(A[0][0]*B[0][1] + A[0][1]*B[1][1])],
        [mod26(A[1][0]*B[0][0] + A[1][1]*B[1][0]), mod26(A[1][0]*B[0][1] + A[1][1]*B[1][1])]
    ]

if __name__ == "__main__":
    # Example: replace with real digrams
    # Plaintext digrams P1="ME", P2="ET"
    P1 = ("M","E")
    P2 = ("E","T")
    # Corresponding ciphertext digrams C1="XG", C2="QJ" as example
    C1 = ("X","G")
    C2 = ("Q","J")

    P = [[ord(P1[0])-65, ord(P2[0])-65],
         [ord(P1[1])-65, ord(P2[1])-65]]
    C = [[ord(C1[0])-65, ord(C2[0])-65],
         [ord(C1[1])-65, ord(C2[1])-65]]

    print("Plain matrix P (columns are P1,P2):")
    print(P)
    print("Cipher matrix C (columns are C1,C2):")
    print(C)

    P_inv = matrix_inverse_2x2(P)
    if P_inv is None:
        raise SystemExit("Plaintext matrix P not invertible mod 26. Need different plaintext digrams.")
    print("P_inv (mod26):")
    print(P_inv)

    K = mat_mult_2x2(C, P_inv)
    print("Recovered key matrix K (mod26):")
    print(K)
