# Caesar Cipher Implementation

def encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift_char = chr((ord(char.lower()) - 97 + shift) % 26 + 97)
            encrypted += shift_char.upper() if char.isupper() else shift_char
        else:
            encrypted += char
    return encrypted

def decrypt(text, shift):
    return encrypt(text, -shift)


message = "Hello, World!"
shift_value = 4

encrypted_message = encrypt(message, shift_value)
print(f"Encrypted Message: {encrypted_message}")

decrypted_message = decrypt(encrypted_message, shift_value)
print(f"Decrypted Message: {decrypted_message}")
