# Muhammad Yusuf Adhi Surya
# 140810220027

import numpy as np

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def matrix_mod_inv(matrix, mod):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = mod_inverse(det % mod, mod)

    if det_inv is None:
        raise ValueError("Inverse doesn't exist")

    adjugate_matrix = np.round(det * np.linalg.inv(matrix)).astype(int) % mod
    inv_matrix = (det_inv * adjugate_matrix) % mod
    return inv_matrix

def hill_encrypt(plaintext, key_matrix, mod=26):
    plaintext = plaintext.replace(" ", "").upper() 
    n = key_matrix.shape[0]  # Size of key matrix
    if len(plaintext) % n != 0:
        plaintext += 'X' * (n - len(plaintext) % n)

    plaintext_vector = [ord(char) - ord('A') for char in plaintext]
    plaintext_matrix = np.array(plaintext_vector).reshape(-1, n)

    encrypted_matrix = (plaintext_matrix.dot(key_matrix) % mod)
    encrypted_text = ''.join([chr(num + ord('A')) for num in encrypted_matrix.flatten()])

    return encrypted_text

def hill_decrypt(ciphertext, key_matrix, mod=26):
    n = key_matrix.shape[0]
    ciphertext = ciphertext.replace(" ", "").upper()

    ciphertext_vector = [ord(char) - ord('A') for char in ciphertext]
    ciphertext_matrix = np.array(ciphertext_vector).reshape(-1, n)

    key_matrix_inv = matrix_mod_inv(key_matrix, mod)

    decrypted_matrix = (ciphertext_matrix.dot(key_matrix_inv) % mod)
    decrypted_text = ''.join([chr(int(num) + ord('A')) for num in decrypted_matrix.flatten()])

    return decrypted_text

def find_key_matrix(plaintext, ciphertext, n=2, mod=26):
    plaintext = plaintext.replace(" ", "").upper()
    ciphertext = ciphertext.replace(" ", "").upper()

    if len(plaintext) != len(ciphertext):
        raise ValueError("Plaintext and ciphertext length must be the same")

    plaintext_vector = [ord(char) - ord('A') for char in plaintext]
    ciphertext_vector = [ord(char) - ord('A') for char in ciphertext]

    p_matrix = np.array(plaintext_vector).reshape(-1, n)
    c_matrix = np.array(ciphertext_vector).reshape(-1, n)

    p_inv = matrix_mod_inv(p_matrix, mod)
    key_matrix = (c_matrix.dot(p_inv) % mod)

    return key_matrix

def main_menu():
    while True:
        print("\nMenu Hill Cipher:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Cari Kunci (Key) dari Plaintext dan Ciphertext")
        print("4. Keluar")
        choice = input("Pilih opsi (1/2/3/4): ")

        if choice == '1':
            plaintext = input("Masukkan teks yang ingin dienkripsi: ").upper()
            key_matrix = input_key_matrix()
            encrypted_text = hill_encrypt(plaintext, key_matrix)
            print(f"Teks yang terenkripsi: {encrypted_text}")

        elif choice == '2':
            ciphertext = input("Masukkan teks yang ingin didekripsi: ").upper()
            key_matrix = input_key_matrix()
            decrypted_text = hill_decrypt(ciphertext, key_matrix)
            print(f"Teks yang didekripsi: {decrypted_text}")

        elif choice == '3':
            plaintext = input("Masukkan plaintext: ").upper()
            ciphertext = input("Masukkan ciphertext: ").upper()
            n = int(input("Masukkan ukuran matriks kunci (contoh: 2 untuk 2x2): "))
            found_key = find_key_matrix(plaintext, ciphertext, n)
            print(f"Matriks kunci yang ditemukan:\n{found_key}")

        elif choice == '4':
            print("Terima kasih! Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def input_key_matrix():
    n = int(input("Masukkan ukuran matriks kunci (contoh: 2 untuk 2x2): "))
    print(f"Masukkan elemen matriks kunci ukuran {n}x{n} (masukkan elemen per baris):")
    
    key_matrix = []
    for i in range(n):
        row = list(map(int, input(f"Masukkan elemen untuk baris {i+1} dipisahkan dengan spasi: ").split()))
        if len(row) != n:
            print("Jumlah elemen yang dimasukkan tidak sesuai dengan ukuran matriks!")
            return input_key_matrix()
        key_matrix.append(row)
    
    key_matrix = np.array(key_matrix)
    key_matrix = key_matrix.T
    return key_matrix


if __name__ == "__main__":
    main_menu()
