# Quellen: https://cryptography.io/en/35.0.0/x509/reference/
#
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from pathlib import Path

# Hier definiere ich die Pfade zum Zertifikat und zum Ordner mit den zuvor entschlüsselten Audiodateien.
cert_path = Path(r"C:\Users\paulh\PycharmProjects\pythonProject\Homework_1\decrypted_archive_OFB\certificate.pem")
audio_dir = Path(r"C:\Users\paulh\PycharmProjects\pythonProject\Homework_1\decrypted_archive_OFB\decrypted_audios")

# Hier lade ich das X.509-Zertifikat und extrahiere den öffentlichen Schlüssel.
with open(cert_path, "rb") as cert_file:
    cert = x509.load_pem_x509_certificate(cert_file.read(), default_backend())
    public_key = cert.public_key()

# Hier wandle ich die Signatur, die ich überprüfen soll, in ein Byte-Format umgewandelt.
signature_hex = "d4f743ad83c57e89ec8b2461bc027c93b2f23b25c8649000bceb061117c764f6991d8fe62d10345c9fe601df841843c695c48e49e4ec239ec93d998adedfd304"
signature_bytes = bytes.fromhex(signature_hex)

# Funktion: Padding von Daten entfernen, da dies aus dem Aufgabenblatt 1 angewandt ist und im Aufgabenblatt 2 wieder entfernt werden soll.
def remove_padding(data):
    return data.rstrip(b'\x00')

# Funktion zur Überprüfung der Signatur
def verify_signature(public_key, signature, data):
    try:
        # Signaturprüfung, bei Ed25519 ist kein Padding notwendig.
        public_key.verify(signature, data)
        return True
    except Exception as e:
        print(e)
        return False

# Hier durchlaufen wir alle WAV-Dateien im angegebenen Verzeichnis und überprüfen die Signatur.
for audio_file in audio_dir.glob("*.wav"):
    with open(audio_file, "rb") as file:
        data = file.read()
        data = remove_padding(data)
    if verify_signature(public_key, signature_bytes, data):
        print(f"Die Signatur stimmt überein mit: {audio_file}")


# Resultat ist:
# Die Signatur stimmt überein mit: C:\Users\paulh\PycharmProjects\pythonProject\Homework_1\decrypted_archive_OFB\decrypted_audios\file_62.wav