# filename: 26_rsa_reuse_modulus_after_d_leak.py
"""
Short demonstration: if d is leaked, DO NOT reuse same modulus n. Generate new p,q,n.
This script just prints the recommendation and why.
"""
print("If Bob leaks his private key d, generating a new (e,d) pair with the SAME modulus n is unsafe.")
print("Reason: knowledge of d may allow recovery of phi(n) or p/q in some attack variants, and reusing modulus")
print("keeps long-term cryptographic links; best practice: generate new primes p,q and new modulus n'.")
