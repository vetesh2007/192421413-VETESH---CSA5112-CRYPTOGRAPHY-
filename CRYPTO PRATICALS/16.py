# filename: 16_monoalphabetic_solver.py
"""
Monoalphabetic substitution solver.
Usage: run script and paste ciphertext when prompted.
"""
import random, math
from collections import Counter

ENGLISH_FREQ = {'E':12.0,'T':9.1,'A':8.2,'O':7.5,'I':7.0,'N':6.7,'S':6.3,'R':6.0,'H':6.1,
                'L':4.0,'D':4.3,'C':2.8,'U':2.8,'M':2.4,'F':2.2,'Y':2.0,'W':2.4,'G':2.0,
                'P':1.9,'B':1.5,'V':1.0,'K':0.8,'X':0.15,'Q':0.1,'J':0.15,'Z':0.07}

def score_text(text):
    cnt = Counter(ch for ch in text.upper() if ch.isalpha())
    total = sum(cnt.values()) or 1
    s = 0.0
    for ch, c in cnt.items():
        s += c * math.log(ENGLISH_FREQ.get(ch, 0.01))
    s -= sum(1 for c in text if not (c.isalpha() or c.isspace())) * 0.5
    return s

def random_key():
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    perm = letters[:]
    random.shuffle(perm)
    return dict(zip(letters, perm))

def apply_key(text, key):
    out=[]
    for ch in text:
        if ch.isalpha():
            mapped = key[ch.upper()]
            out.append(mapped.lower() if ch.islower() else mapped)
        else:
            out.append(ch)
    return "".join(out)

def tweak_key(key):
    a,b = random.sample(list(key.keys()),2)
    nk = key.copy()
    nk[a], nk[b] = nk[b], nk[a]
    return nk

def hillclimb(ciphertext, restarts=200, iters=1500, top_n=5):
    candidates=[]
    for _ in range(restarts):
        key = random_key()
        plain = apply_key(ciphertext, key)
        s = score_text(plain)
        for _ in range(iters):
            k2 = tweak_key(key)
            p2 = apply_key(ciphertext, k2)
            s2 = score_text(p2)
            if s2 > s or random.random() < 0.001:
                key, s, plain = k2, s2, p2
        candidates.append((s, plain))
    candidates.sort(reverse=True, key=lambda x: x[0])
    return candidates[:top_n]

def main():
    print("Monoalphabetic solver. Paste ciphertext and press Enter:")
    ct = input().strip()
    top = hillclimb(ct, restarts=200, iters=1500, top_n=10)
    for i,(s,p) in enumerate(top,1):
        print(f"#{i} score={s:.2f}\n{p}\n")

if __name__ == "__main__":
    main()
