def generate_valid_keys():
    valid_keys = []

    # Iteriere durch alle möglichen Byte-Werte
    for original_byte in range(256):
        # Hier wende ich die gegebenen Operationen aus der Aufgabe an:
        # XOR mit 0xFF: Diese Operation invertiert jedes Bit des Schlüssels. Wenn ein Bit ursprünglich 1 war, wird es zu 0 und andersherum.
        # UND mit 60: Die binäre Darstellung von 60 ist 0011 1100. Diese Operation setzt alle Bits außer den vier Bits in der Mitte auf 0. Nur die Bits 3, 4, 5 und 6 können Einsen sein.
        # ODER mit 0x81: Die binäre Darstellung von 0x81 ist 1000 0001. Diese Operation setzt das höchste und das niedrigste Bit im Byte auf 1, unabhängig von ihrem vorherigen Zustand.
        # Linksverschiebung um 5: Bei dieser Operation werden alle Bits um fünf Stellen nach links verschoben. Das bedeutet, dass die oberen fünf Bits verloren gehen und die unteren fünf Bits auf Null gesetzt werden.

        # XOR mit 0xFF
        key_byte = original_byte ^ 0xFF
        # AND mit 60 (0011 1100)
        key_byte = key_byte & 0x3C
        # OR mit 0x81 (1000 0001)
        key_byte = key_byte | 0x81
        # Left Shift um 5
        key_byte = (key_byte << 5) & 0xFF  # Maskiere mit 0xFF, um nur das untere Byte zu behalten für "<< 5 //leftshift , no rotation".
        # Füge das resultierende Byte zur Liste hinzu
        valid_keys.append(key_byte)

    return valid_keys


valid_key_bytes = generate_valid_keys()
print("Gültige Schlüsselbytes:")
for byte in set(valid_key_bytes):  # "set" um nur einzigartige Werte zu zeigen, welche somit die Möglichkeiten sind.
    print(f"0x{byte:02X}")
print(f"Anzahl der eindeutigen gültigen Schlüsselbytes: {len(set(valid_key_bytes))}")
