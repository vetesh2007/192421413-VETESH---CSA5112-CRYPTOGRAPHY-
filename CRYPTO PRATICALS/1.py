def caesar_cipher(text, k):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + k) % 26 + shift)
        else:
            result += char
    return result

# Example
plaintext = input("Enter plaintext: ")
k = int(input("Enter shift (1–25): "))
ciphertext = caesar_cipher(plaintext, k)
print("Encrypted text:", ciphertext)

output:
Enter plaintext: HELLO WORLD
Enter shift (1-25): 3
Encrypted text: KHOOR ZRUOG

