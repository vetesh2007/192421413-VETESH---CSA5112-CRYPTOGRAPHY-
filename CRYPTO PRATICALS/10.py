# ------------------------------
# Question 10: Encrypt message using given Playfair Matrix
# ------------------------------

def find_pos(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j
    return None


def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = "".join(ch for ch in text if ch.isalpha())
    digraphs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else "X"
        if a == b:
            digraphs.append(a + "X")
            i += 1
        else:
            digraphs.append(a + b)
            i += 2
    return digraphs


def playfair_encrypt(plaintext, matrix):
    digraphs = prepare_text(plaintext)
    result = ""

    for pair in digraphs:
        a, b = pair[0], pair[1]
        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)

        if r1 == r2:
            result += matrix[r1][(c1 + 1) % 5]
            result += matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            result += matrix[(r1 + 1) % 5][c1]
            result += matrix[(r2 + 1) % 5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]
    return result


# --- Given matrix from question ---
matrix = [
    ['M', 'F', 'H', 'I', 'K'],
    ['U', 'N', 'O', 'P', 'Q'],
    ['Z', 'V', 'W', 'X', 'Y'],
    ['E', 'L', 'A', 'R', 'G'],
    ['D', 'S', 'T', 'B', 'C']
]

print("Given Playfair Matrix:")
for row in matrix:
    print(row)

# --- Encrypt the message ---
message = "Must see you over Cadogan West. Coming at once."
cipher_text = playfair_encrypt(message, matrix)
print("\nEncrypted Message:")
print(cipher_text)

output:
Given Playfair Matrix:
['M', 'F', 'H', 'I', 'K']
['U', 'N', 'O', 'P', 'Q']
['Z', 'V', 'W', 'X', 'Y']
['E', 'L', 'A', 'R', 'G']
['D', 'S', 'T', 'B', 'C']

Encrypted Message:
UZTBDLGZPNNW LGTGTUERGVLDBDUHFPERHWQSRZ
