import numpy as np
import cv2

file_path = r'C:\Users\paulh\PycharmProjects\pythonProject\Homework_1\password.rgba'
# Hier versuche ich, die Datei als rohe Bytefolge zu laden
try:
    raw_data = np.fromfile(file_path, dtype=np.uint8)
    # Hier konvertiere ich die Rohdaten in ein Bild (600x600 mit 4 Kanälen, da RGBA)
    image = raw_data.reshape((600, 600, 4))
    # Ich prüfe, ob das Bild korrekt geladen wurde.
    # Dann zeige ich das Bild an und warte auf einen Tastendruck
    if image is not None:
        cv2.imshow('Verschlüsseltes Bild', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Fehler beim Laden des Bildes")

except Exception as e:
    print(f"Fehler beim Laden der Datei: {e}")

# Resultat: Das Bild zeigt eine Ente