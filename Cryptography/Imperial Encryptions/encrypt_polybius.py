def generate_polybius_square():
    # Generate the Polybius Square grid
    polybius_square = [['A', 'B', 'C', 'D', 'E'],
                       ['F', 'G', 'H', 'I/J', 'K'],
                       ['L', 'M', 'N', 'O', 'P'],
                       ['Q', 'R', 'S', 'T', 'U'],
                       ['V', 'W', 'X', 'Y', 'Z']]
    return polybius_square

def encrypt_polybius_square(plaintext, polybius_square):
    ciphertext = ''
    
    # Convert the plaintext to uppercase
    plaintext = plaintext.upper()

    # Remove any whitespace from the plaintext
    plaintext = plaintext.replace(' ', '')

    # Encrypt each letter of the plaintext
    for letter in plaintext:
        if letter == 'J':
            letter = 'I'  # Replace 'J' with 'I' in the plaintext
        # Find the letter in the Polybius Square grid and get its coordinates
        for row in range(len(polybius_square)):
            for col in range(len(polybius_square[row])):
                if polybius_square[row][col] == letter:
                    # Convert the coordinates to a pair of numbers and add them to the ciphertext
                    ciphertext += str(row + 1) + str(col + 1)

    return ciphertext

# Define the Polybius Square grid
polybius_square = generate_polybius_square()

# Define the given plaintext
plaintext = "CONGRATULATIONS YOU HAVE SOLVED THE ADVANCED CRYPTOGRAPHY CHALLENGE"

# Encrypt the plaintext using the Polybius Square grid
ciphertext = encrypt_polybius_square(plaintext, polybius_square)

# Print the generated ciphertext
print("Generated Ciphertext:", ciphertext)
