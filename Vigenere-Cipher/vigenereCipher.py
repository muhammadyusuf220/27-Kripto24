def encrypt_vigenere(message, secret_key):
    encrypted_message = []
    key_length = len(secret_key)
    key_index = 0

    for character in message:
        if character.isalpha():
            base = ord('a') if character.islower() else ord('A')
            key_character = ord(secret_key[key_index % key_length].lower()) - ord('a')
            encrypted_message.append(chr((ord(character) - base + key_character) % 26 + base))
            key_index += 1
        else:
            encrypted_message.append(character)
    return ''.join(encrypted_message)

def decrypt_vigenere(encrypted_message, secret_key):
    decrypted_message = []
    key_length = len(secret_key)
    key_index = 0

    for character in encrypted_message:
        if character.isalpha():
            base = ord('a') if character.islower() else ord('A')
            key_character = ord(secret_key[key_index % key_length].lower()) - ord('a')
            decrypted_message.append(chr((ord(character) - base - key_character + 26) % 26 + base))
            key_index += 1
        else:
            decrypted_message.append(character)
    return ''.join(decrypted_message)

def handle_file_operations(file_path, secret_key, is_encrypting=True):
    try:
        with open(file_path, 'r') as input_file:
            content = input_file.read()
    except FileNotFoundError:
        print(f"Error: Tidak dapat membuka file {file_path}")
        return

    processed_result = encrypt_vigenere(content, secret_key) if is_encrypting else decrypt_vigenere(content, secret_key)

    with open('result.txt', 'w') as output_file:
        output_file.write(processed_result)

    print(f"{'Enkripsi' if is_encrypting else 'Dekripsi'} berhasil. Hasil disimpan di result.txt")

def derive_key_from_plain_and_cipher(plain_text, cipher_text):
    derived_key = []
    length = len(plain_text)

    for i in range(length):
        if plain_text[i].isalpha() and cipher_text[i].isalpha():
            key_char = (ord(cipher_text[i].lower()) - ord(plain_text[i].lower()) + 26) % 26
            derived_key.append(chr(key_char + ord('a')) if plain_text[i].islower() else chr(key_char + ord('A')))
        else:
            derived_key.append(' ')  # Tambahkan spasi jika bukan huruf

    return ''.join(derived_key)

def main_menu():
    while True:
        print("\nINI ADALAH PROGRAM VIGENERE CIPHER!")
        print("\nMenu:") 
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Enkripsi dengan file")
        print("4. Dekripsi dengan file")
        print("5. Cari kunci dari ciphertext dan plaintext")
        print("6. Keluar")
        choice = input("Pilih opsi: ")

        if choice == '6':
            print("\nTERIMA KASIH SUDAH MENGGUNAKAN PROGRAM INI!\n")
            break

        secret_key = ""
        message = ""
        plain_text = ""
        cipher_text = ""
        
        if choice == '1':
            secret_key = input("Masukkan kunci: ")
            message = input("Masukkan Plaintext: ")
            print("Hasil enkripsi:", encrypt_vigenere(message, secret_key))
        elif choice == '2':
            secret_key = input("Masukkan kunci: ")
            message = input("Masukkan Ciphertext: ")
            print("Hasil dekripsi:", decrypt_vigenere(message, secret_key))
        elif choice == '3':
            file_path = input("Masukkan nama file untuk enkripsi: ")
            secret_key = input("Masukkan kunci: ")
            handle_file_operations(file_path, secret_key, True)
        elif choice == '4':
            file_path = input("Masukkan nama file untuk dekripsi: ")
            secret_key = input("Masukkan kunci: ")
            handle_file_operations(file_path, secret_key, False)
        elif choice == '5':
            plain_text = input("Masukkan plaintext: ")
            cipher_text = input("Masukkan ciphertext: ")
            if len(plain_text) != len(cipher_text):
                print("Panjang plaintext dan ciphertext harus sama!")
            else:
                print("Perkiraan kunci:", derive_key_from_plain_and_cipher(plain_text, cipher_text))
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == '__main__':
    main_menu()
