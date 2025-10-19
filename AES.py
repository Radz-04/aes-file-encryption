from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os

def encrypt_file(file_path, key):
    if not os.path.isfile(file_path):
        print("Non è stato trovato il File:", file_path)
        return None

    output_path = file_path + ".enc"
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    with open(file_path, 'rb') as f:
        plaintext = f.read()
        padded_data = pad(plaintext, AES.block_size)
        ciphertext = cipher.encrypt(padded_data)

    with open(output_path, 'wb') as f:
        f.write(iv + ciphertext)

    print("Il File cifrato è stato salvato in:", output_path)
    return output_path


def decrypt_file(file_path, key):
    if not os.path.isfile(file_path):
        print("Non è stato trovato il File:", file_path)
        return None

    if not file_path.endswith(".enc"):
        print("Il file non sembra essere cifrato correttamente (manca estensione .enc):", file_path)
        return None

    output_path = file_path[:-4]

    with open(file_path, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext = cipher.decrypt(ciphertext)

    try:
        plaintext = unpad(padded_plaintext, AES.block_size)
    except ValueError:
        print("Errore di padding. La chiave potrebbe essere errata o il file corrotto.")
        return None

    with open(output_path, 'wb') as f:
        f.write(plaintext)

    print("Il File decifrato è stato salvato in:", output_path)
    return output_path



key = b"ThisIsA16ByteKey"
file_path = r"C:\Users\utente\Desktop\text.txt"

encrypted_file = encrypt_file(file_path, key)
if encrypted_file:
    decrypt_file(encrypted_file, key)
