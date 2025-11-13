# additive_cipher_frequency_attack.py
# Performs letter frequency attack on an additive (Caesar) cipher.
# Ranks top-N most likely plaintexts automatically.

import string
from collections import Counter

# English letter frequencies (approximate, normalized)
ENGLISH_FREQ = {
    'A': 8.17, 'B': 1.49, 'C': 2.78, 'D': 4.25, 'E': 12.70,
    'F': 2.23, 'G': 2.02, 'H': 6.09, 'I': 6.97, 'J': 0.15,
    'K': 0.77, 'L': 4.03, 'M': 2.41, 'N': 6.75, 'O': 7.51,
    'P': 1.93, 'Q': 0.10, 'R': 5.99, 'S': 6.33, 'T': 9.06,
    'U': 2.76, 'V': 0.98, 'W': 2.36, 'X': 0.15, 'Y': 1.97,
    'Z': 0.07
}

def shift_text(ciphertext, shift):
    """Shift text backward by given key (0-25)."""
    result = []
    for ch in ciphertext:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            new = (ord(ch.upper()) - ord('A') - shift) % 26
            result.append(chr(new + base))
        else:
            result.append(ch)
    return ''.join(result)

def text_frequency_score(text):
    """Compute chi-squared statistic to compare text letter freq to English."""
    text = [ch.upper() for ch in text if ch.isalpha()]
    if not text:
        return float('inf')
    count = Counter(text)
    total = sum(count.values())
    chi2 = 0.0
    for letter, expected_freq in ENGLISH_FREQ.items():
        observed = count.get(letter, 0)
        expected = total * (expected_freq / 100)
        chi2 += (observed - expected) ** 2 / (expected + 1e-9)
    return chi2

def frequency_attack(ciphertext, top_n=10):
    """Try all 26 keys and rank by frequency match (lower chi2 = better)."""
    results = []
    for key in range(26):
        decrypted = shift_text(ciphertext, key)
        score = text_frequency_score(decrypted)
        results.append((score, key, decrypted))
    results.sort(key=lambda x: x[0])
    print(f"\nTop {top_n} most likely plaintexts:\n")
    for i, (score, key, pt) in enumerate(results[:top_n], start=1):
        print(f"{i:2d}. Key = {key:2d} | Score = {score:10.3f} | Plaintext guess:\n   {pt}\n")

if __name__ == "__main__":
    print("=== Additive (Caesar) Cipher Frequency Attack ===")
    ciphertext = input("Enter ciphertext: ").strip()
    try:
        top_n = int(input("How many top guesses to display? (e.g., 10): "))
    except:
        top_n = 10

    if not ciphertext:
        print("No ciphertext entered. Exiting.")
    else:
        frequency_attack(ciphertext, top_n)
