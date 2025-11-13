# playfair_keyspace.py
# Compute 25! and adjusted key counts and express as powers of 2.

import math

def factorial_log2(n):
    # use log2 of factorial via log gamma for accuracy
    # log2(n!) = log2(gamma(n+1)) = ln(gamma(n+1)) / ln(2)
    ln_fact = math.lgamma(n + 1)
    return ln_fact / math.log(2)

def approx_value(n):
    # approximate value of n! using exp(lgamma)
    val = math.exp(math.lgamma(n + 1))
    return val

if __name__ == "__main__":
    n = 25
    log2_25_fact = factorial_log2(25)
    log2_24_fact = factorial_log2(24)

    print(f"25!  ≈ 2^{log2_25_fact:.6f}")
    print(f"24!  ≈ 2^{log2_24_fact:.6f}")
    # also show scientific approximations (may be large)
    approx_25 = approx_value(25)
    approx_24 = approx_value(24)
    print(f"25!  ≈ {approx_25:.6e}")
    print(f"24!  ≈ {approx_24:.6e}")

    print("\nInterpretation:")
    print(f" - Ignoring equivalent keys: ~25! ≈ 2^{log2_25_fact:.2f}")
    print(f" - Accounting for a simple division by 25 (~cyclic shifts): ~25!/25 = 24! ≈ 2^{log2_24_fact:.2f}")
