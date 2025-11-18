# filename: 28_diffie_hellman_demo.py
"""
Diffie-Hellman demo.
Also explains why sending x*a mod q (multiplication) would be insecure.
"""
import random

def dh_demo():
    q = 2087  # small prime for demo
    a = 5
    alice = random.randint(2, q-2)
    bob = random.randint(2, q-2)
    A = pow(a, alice, q)
    B = pow(a, bob, q)
    alice_shared = pow(B, alice, q)
    bob_shared = pow(A, bob, q)
    print("Shared equal?", alice_shared == bob_shared)

if __name__=='__main__':
    dh_demo()
    print("\nIf participants sent x*a mod q (multiplication) rather than exponentiation, the scheme loses discrete-log hardness.")
    print("Multiplication leaks linear information and is trivial to invert in many cases; it is insecure.")

