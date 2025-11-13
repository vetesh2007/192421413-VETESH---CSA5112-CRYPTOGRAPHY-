# otp_vigenere.py
# One-time-pad style Vigenere: numeric keystream

def strip_and_upper(s):
    return ''.join(ch for ch in s.upper() if ch.isalpha())

def mod26(x): return x % 26

def encrypt(pt, keystream):
    ct_chars = []
    for i, ch in enumerate(pt):
        p = ord(ch) - 65
        k = keystream[i]
        c = mod26(p + k)
        ct_chars.append(chr(c + 65))
        print(f"p={ch}({p:2d}) k={k:2d} -> c={chr(c+65)}({c:2d})")
    return ''.join(ct_chars)

def recover_keystream(ct, target_plain):
    ks = []
    for i, ch in enumerate(target_plain):
        c = ord(ct[i]) - 65
        p = ord(ch) - 65
        k = mod26(c - p)  # because p + k = c  (mod26) -> k = c - p
        ks.append(k)
        print(f"pos {i:2d}: c={ct[i]}({c:2d}) p={ch}({p:2d}) -> k={k:2d}")
    return ks

if __name__ == "__main__":
    pt_raw = "send more money"
    pt = strip_and_upper(pt_raw)
    keystream = [9,0,1,7,23,15,21,14,11,11,2,8,9]  # given
    print("Plaintext (letters only):", pt)
    print("\nEncryption:")
    ct = encrypt(pt, keystream)
    print("\nCiphertext:", ct)

    print("\n--- Key recovery example ---")
    target_raw = "cash not needed"
    target = strip_and_upper(target_raw)
    print("Target plaintext:", target)
    # Use ciphertext produced earlier. If ciphertext length > target length, we'll only use min length.
    ct_for_recovery = ct
    L = min(len(ct_for_recovery), len(target))
    print("\nRecovered keystream for target (positions 0..{}):".format(L-1))
    recovered = recover_keystream(ct_for_recovery[:L], target[:L])
    print("Recovered keystream (first {} items):".format(L), recovered)
