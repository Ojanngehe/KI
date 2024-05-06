def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    text = input("Masukkan teks yang ingin dienkripsi: ")
    shift = int(input("Masukkan jumlah pergeseran (bilangan bulat): "))

    encrypted_text = encrypt(text, shift)
    print("Teks terenkripsi:", encrypted_text)

    decrypted_text = decrypt(encrypted_text, shift)
    print("Teks terdekripsi:", decrypted_text)

if __name__ == "__main__":
    main()