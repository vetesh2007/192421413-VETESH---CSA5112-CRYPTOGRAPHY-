def mod_inverse(a, m):
    """Return modular inverse of a mod m, if exists."""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def solve_affine_from_freq(C1, C2, P1, P2):
    # Convert letters to numbers (A=0,...,Z=25)
    C1, C2 = ord(C1.upper()) - 65, ord(C2.upper()) - 65
    P1, P2 = ord(P1.upper()) - 65, ord(P2.upper()) - 65

    # (C1 - C2) ≡ a * (P1 - P2) mod 26
    diff_P = (P1 - P2) % 26
    diff_C = (C1 - C2) % 26

    inv = mod_inverse(diff_P, 26)
    if inv is None:
        print("No valid inverse; cannot solve for 'a'.")
        return None, None

    a = (diff_C * inv) % 26
    b = (C1 - a * P1) % 26
    return a, b

# Given values
C1, C2 = 'B', 'U'  # most frequent ciphertext letters
P1, P2 = 'E', 'T'  # assume they map to 'E' and 'T'

a, b = solve_affine_from_freq(C1, C2, P1, P2)
print(f"Derived affine cipher parameters: a = {a}, b = {b}")

output:
Derived affine cipher parameters: a = 3, b = 15
