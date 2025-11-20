def affine_encrypt(plaintext, a, b):
    result = ""
    for char in plaintext.upper():
        if char.isalpha():
            P = ord(char) - 65
            C = (a * P + b) % 26
            result += chr(C + 65)
        else:
            result += char
    return result

# Check for valid 'a'
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example
plaintext = input("Enter plaintext: ")
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

if gcd(a, 26) != 1:
    print("Invalid 'a' value. 'a' must be coprime with 26 for decryption to be possible.")
else:
    ciphertext = affine_encrypt(plaintext, a, b)
    print("Ciphertext:", ciphertext)

output:
Enter plaintext: AFFINECIPHER
Enter value of a: 5
Enter value of b: 8
Ciphertext: IHHWVCSWFRCP

