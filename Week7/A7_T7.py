ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def load_config(filename):
    rotors = []
    reflector = ""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or ":" not in line:
                continue
            label, mapping = line.split(":", 1)
            mapping = mapping.strip().upper()
            if label.strip().startswith("Rotor"):
                rotors.append(mapping)
            elif label.strip().startswith("Reflector"):
                reflector = mapping
    return rotors, reflector

def step(positions):
    positions[0] += 1
    if positions[0] == 26:
        positions[0] = 0
        positions[1] += 1
        if positions[1] == 26:
            positions[1] = 0
            positions[2] += 1
            if positions[2] == 26:
                positions[2] = 0

def forward(idx, rotors, pos):
    for r in range(3):
        shifted = (idx + pos[r]) % 26
        mapped_char = rotors[r][shifted]
        idx = ALPHABET.index(mapped_char)
    return idx

def reflect(idx, reflector):
    # Single pass through reflector mapping
    mapped_char = reflector[idx]
    return ALPHABET.index(mapped_char)

def reverse(idx, rotors, pos):
    for r in (2, 1, 0):
        target_char = ALPHABET[idx]
        k = rotors[r].index(target_char)
        idx = (k - pos[r]) % 26
    return idx

def main():
    config_file = input("Insert config(filename): ")
    rotors, reflector = load_config(config_file)

    _ = input("Insert plugs (y/n)?: ")
    print("No extra plugs inserted.")
    print("Enigma initialized.")
    print()
    while True:
        row = input("Insert row (empty stops): ").strip().upper()
        if row == "":
            break
        positions = [0, 0, 0]
        converted_chars = []
        for ch in row:
            if ch not in ALPHABET:
                continue
            step(positions)
            idx = ALPHABET.index(ch)
            idx = forward(idx, rotors, positions)
            idx = reflect(idx, reflector)
            idx = reverse(idx, rotors, positions)
            out_ch = ALPHABET[idx]
            print(f"Character:'{ch}', illuminated as '{out_ch}'")
            converted_chars.append(out_ch)
        converted = "".join(converted_chars)
        print(f"Converted row - '{converted}'")
        print()  
    print("Enigma closing.")

if __name__ == "__main__":
    main()
