def generate_polybius_square():
    # Generate the Polybius Square grid
    polybius_square = [['A', 'B', 'C', 'D', 'E'],
                       ['F', 'G', 'H', 'I/J', 'K'],
                       ['L', 'M', 'N', 'O', 'P'],
                       ['Q', 'R', 'S', 'T', 'U'],
                       ['V', 'W', 'X', 'Y', 'Z']]
    return polybius_square

def decrypt_polybius_square(ciphertext, polybius_square):
    decrypted_text = ''

    # Remove any whitespace from the ciphertext
    ciphertext = ciphertext.replace(' ', '')

    # Split the ciphertext into pairs of numbers
    pairs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]

    # Decrypt each pair of numbers
    for pair in pairs:
        if len(pair) == 2:  # Check if the pair has two digits
            row = int(pair[0]) - 1
            col = int(pair[1]) - 1
            decrypted_text += polybius_square[row][col]

    return decrypted_text

# Define the Polybius Square grid
polybius_square = generate_polybius_square()

# Define the given ciphertext
ciphertext = "1334332242114445311144343343543445231151154334315115144423151114511133131514134254354434224211352354132311313115332215"

# Decrypt the ciphertext using the Polybius Square grid
plaintext = decrypt_polybius_square(ciphertext, polybius_square)

# Print the decrypted plaintext message
print("Decrypted Message:", plaintext)
