# Quellen:  https://docs.fileformat.com/audio/wav/
#           https://cryptography.io/en/3.0/_modules/cryptography/hazmat/primitives/ciphers/algorithms/
#           https://cryptography.io/en/42.0.5/hazmat/backends/
import os
from itertools import product
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def generate_all_possible_keys():
    valid_bytes = [0xA0, 0x20]  # Die zwei eindeutigen gültigen Schlüsselbytes aus dem Code davor.
    key_length = 16  # AES-128 Schlüssels in Bytes
    # Generiere alle möglichen Kombinationen der gültigen Bytes
    all_keys = list(product(valid_bytes, repeat=key_length))
    # Konvertiere die Tuple-Liste in eine Liste von Bytearrays
    all_keys = [bytes(key) for key in all_keys]
    return all_keys

def check_wav_header(data):
    # So sieht eine .wav header typischerweise aus. (Quelle: https://docs.fileformat.com/audio/wav/)
    return data[:4] == b'RIFF' and data[8:12] == b'WAVE'

def decrypt_and_save_files(input_dir, output_dir, keys):
    # Iteriere durch alle Dateien im Ordner
    for filename in os.listdir(input_dir):
        if filename.endswith(".enc"):
            input_file_path = os.path.join(input_dir, filename)
            output_file_path = os.path.join(output_dir, os.path.splitext(filename)[0] + ".wav")

            with open(input_file_path, 'rb') as encrypted_file:
                encrypted_data = encrypted_file.read()

            for key in keys:
                cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
                decryptor = cipher.decryptor()
                decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

                if check_wav_header(decrypted_data):
                    with open(output_file_path, 'wb') as wav_file:
                        wav_file.write(decrypted_data)
                    print(f"Erfolgreich entschlüsselt {input_file_path} mit Schlüssel: {key.hex()}")
                    break  # Stoppt die Schleife, wenn ein gültiger Schlüssel gefunden wurde
            else:
                print(f"Kein gültiger Schlüssel gefunden für {input_file_path}")

all_possible_keys = generate_all_possible_keys()

input_directory = r'C:\Users\paulh\PycharmProjects\pythonProject\Homework_1\decrypted_archive_OFB\encrypted_audios'
output_directory = r'C:\Users\paulh\PycharmProjects\pythonProject\Homework_1\decrypted_archive_OFB\decrypted_audios'

decrypt_and_save_files(input_directory, output_directory, all_possible_keys)

# Resultat: alle Dateien wurden erfolgreich entschlüsslt und im Ornder decrypted_audios gespeichert.
# Ich habe die Dateien beispielhaft geöffnet um zu schauen ob es einen ton gibt, dies hat funktioniert.