# ------------------------------
# Question 9: PT-109 Decryption using Playfair Cipher
# ------------------------------

def generate_matrix(keyword):
    keyword = keyword.upper().replace("J", "I")
    matrix = []
    seen = set()

    for ch in keyword:
        if ch.isalpha() and ch not in seen:
            seen.add(ch)
            matrix.append(ch)
    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in seen:
            seen.add(ch)
            matrix.append(ch)
    return [matrix[i:i+5] for i in range(0, 25, 5)]


def find_pos(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j
    return None


def process_text(text):
    text = text.upper().replace("J", "I")
    return "".join(ch for ch in text if ch.isalpha())


def playfair_decrypt(cipher, matrix):
    cipher = process_text(cipher)
    result = ""

    for i in range(0, len(cipher), 2):
        a, b = cipher[i], cipher[i+1]
        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)

        if r1 == r2:
            result += matrix[r1][(c1 - 1) % 5]
            result += matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:
            result += matrix[(r1 - 1) % 5][c1]
            result += matrix[(r2 - 1) % 5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]
    return result


# --- Decrypt PT-109 Message ---
cipher_text = """
KXJEY UREBE ZWEHE WRYTU HEYFS
KREHE GOYFI WTTTU OLKSY CAJPO
BOTEI ZONTX BYBNT GONEY CUZWR
GDSON SXBOU YWRHE BAAHY USEDQ
"""

# Known key phrase for PT-109 = "ROYAL NEW ZEALAND NAVY"
matrix = generate_matrix("ROYALNEWZEALANDNAVY")

# Print the Playfair matrix
print("Playfair Matrix (PT-109):")
for row in matrix:
    print(row)

# Decrypt
plain_text = playfair_decrypt(cipher_text, matrix)
print("\nDecrypted PT-109 Message:")
print(plain_text)

output:
Playfair Matrix (PT-109):
['R', 'O', 'Y', 'A', 'L']
['N', 'E', 'W', 'Z', 'D']
['V', 'B', 'C', 'F', 'G']
['H', 'I', 'K', 'M', 'P']
['Q', 'S', 'T', 'U', 'X']

Decrypted PT-109 Message:
PTBOATONEOWENINELOSTINACTIONINBLACKESSSTRAITTWOMILESSWERESUCGVEXCREWOF TWELVEXR
QUESTANYINFORMATIONX
