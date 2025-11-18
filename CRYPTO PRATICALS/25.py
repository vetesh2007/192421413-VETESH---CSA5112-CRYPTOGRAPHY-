# filename: 25_rsa_gcd_plaintext_factor.py
"""
If a plaintext block m shares nontrivial gcd with n, gcd(m,n) may reveal a factor of n.
"""
import math

def gcd_factor(m,n):
    g = math.gcd(m,n)
    if 1 < g < n:
        return g
    return None

if __name__=='__main__':
    n = int(input("n = ").strip())
    m = int(input("known plaintext block m = ").strip())
    g = gcd_factor(m,n)
    if g:
        print("Nontrivial factor found:", g)
    else:
        print("No nontrivial factor from gcd(m,n).")
