# Quellen:  https://cryptography.io/en/3.0/_modules/cryptography/hazmat/primitives/ciphers/algorithms/
#           https://cryptography.io/en/42.0.5/hazmat/backends/
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Von der vorherigen Aufgabe weiß ich, dass das Passwort etwas mit "Ente" zu tun hat.
# Also habe ich versucht: "Duck, duck, Ente, ente". "ente" hat dann geklappt
password = b'ente'
# Padding muss auf 128 Bit = 16 Bytes gesetzt werden
key_length = 16
padded_password = password.ljust(key_length, b'\x00')

file_path = 'C:/Users/paulh/PycharmProjects/pythonProject/Homework_1/archive.enc'
output_base_path = 'C:/Users/paulh/PycharmProjects/pythonProject/Homework_1/'

# Initialisierungsvektor (IV), der auch 128 Bit (16 Bytes) lang sein muss!
iv = b'\x00' * 16
# Funktion: zur Entschlüsselung mit den verschiedenen AES Modi die in der Aufgabenstellung genannt wurden.
def decrypt_aes(data, key, iv, mode):
    cipher = Cipher(algorithms.AES(key), mode(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(data) + decryptor.finalize()
    return decrypted_data

try:
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()
except FileNotFoundError:
    print(f"Die Datei {file_path} wurde nicht gefunden.")
    encrypted_data = b''

modes_to_try = [modes.OFB, modes.CFB, modes.CBC]

for mode in modes_to_try:
    output_zip_path = os.path.join(output_base_path, f'decrypted_archive_{mode.__name__}.zip')
    print(f"Versuche Modus: {mode.__name__}")
    try:
        decrypted_data = decrypt_aes(encrypted_data, padded_password, iv, mode)
        with open(output_zip_path, 'wb') as zip_file:
            zip_file.write(decrypted_data)
        print(f"Entschlüsselte Daten wurden als ZIP unter {output_zip_path} gespeichert.")
    except Exception as e:
        print(f"Fehler beim Entschlüsseln mit {mode.__name__}: {str(e)}")

# Resultat: Ich habe 3 Zip dateien bekommen (siehe Verzeichnis). Es lies sich nur die OFB öffnen, daher OFB.