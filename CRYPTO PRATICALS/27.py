# filename: 27_rsa_per_char_attack.py
"""
Demonstrate that encrypting each letter 0..25 separately is weak; attacker can brute-force each ciphertext.
This script creates small RSA and shows brute-force recovery.
"""
def powmod(a,e,n): return pow(a,e,n)

def brute_force_block(c,e,n,alphabet_size=26):
    res=[]
    for m in range(alphabet_size):
        if pow(m,e,n)==c:
            res.append(m)
    return res

if __name__=='__main__':
    e = int(input("e = ").strip()); n = int(input("n = ").strip())
    block_count = int(input("number of cipher blocks = ").strip())
    blocks = [int(input(f"c[{i}] = ").strip()) for i in range(block_count)]
    for i,c in enumerate(blocks):
        cand = brute_force_block(c,e,n)
        print(f"Block {i} candidates: {cand}")
    print("\nIf candidates are small (like 1 each), attacker recovers plaintext easily. Use padding or larger message blocks.")
