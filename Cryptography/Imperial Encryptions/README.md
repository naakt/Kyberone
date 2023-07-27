# Imperial Cipher (Easy)

## Challenge:
Welcome, brave recruits of the Rebellion! As valiant defenders of freedom and justice, you have been chosen to undertake a series of challenges that will test your mettle and cunning in the realm of cryptography.

In this galaxy-spanning adventure, you will assume the role of skilled operatives working to protect sensitive Rebel communications from falling into the hands of the Empire. Through your mastery of encryption techniques, you will thwart the Empire's surveillance and ensure the safety of vital information crucial to our cause.

Today, we present you with the first challenge. Decrypt the encoded message intercepted from Imperial spies to uncover hidden intelligence. Within this secret communiqué lies information that could turn the tide in our favor.

Your mission, should you choose to accept it, is to unravel the encryption and reveal the true message. Beware, for the Empire is always watching, and failure is not an option.

Prepare yourself, as more challenges and advanced cryptographic techniques await you in the battles to come. The fate of the Rebellion rests in your hands. May the Force be with you, brave codebreaker!

Encrypted Message: "GTQTA RTAA WPH QTTC ADRPITS DC SPCIDDXCT, XBETGXPA UDGRTH EGTEPGTS ID PIIPRZ"

## Solution:
A Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of positions down or up the alphabet. In this case, the message is shifted 15 positions up the alphabet.

Decrypted Message: "REBEL CELL HAS BEEN LOCATED ON DANTOOINE, IMPERIAL FORCES PREPARED TO ATTACK"


# The Veiled Vigenere (Medium)

## Challenge:
Congratulations on your success in deciphering the Caesar cipher, brave codebreaker! Your skills are truly exceptional. Our forces have evacuated successfully. Now, prepare yourself for the next cryptographic challenge in our Rebellion mission.

This time, we present you with an encrypted message that has been encoded using a more complex technique known as the Vigenere cipher. The Vigenere cipher involves using a keyword to determine the shifting pattern for each letter in the plaintext.

Encrypted Message: "ZQQIC NOCKQH LRDE PDMSIU. I TCIOZII PAD JQTR GTANMP DR FVE ZN FWIZZ SSQBH. XYM SNCY PTGMAC BA QI ZV TSM KPZZV SJAFTQ. WWLWWI PRU LEDBDDC."

Intelligence tells us that the first word of the encoded message has a high likelihood of being REBEL.

Your task is to decrypt the encoded message using the Vigenere cipher and unveil its hidden meaning. The fate of the Rebellion may hinge upon the intelligence concealed within this communication.

Stay vigilant, for the Empire's agents are always watching. May your deciphering skills be sharp, and may the Force guide you in unraveling the secrets of the Veiled Vigenere.

Decode the message and proceed with haste, for more challenges await in our fight for freedom!

## Hint
Intelligence tells us that the key may have been in the previous intercept you decoded.

## Solution:
The Vigenère cipher is a polyalphabetic substitution cipher that uses a keyword to encrypt and decrypt the message. To decrypt the message, you need to apply the reverse operation using the key "IMPERIAL".

We can get the first 5 letters are IMPER. This decodes the message to:
REBEL FCNGZZ ZCZN HRXORM. W EYRGNTE YSR UMCJ UEWWED ON ONS KJ OOWKV BKEMD. GQA DJLQ DECVSQ MW ZA NG PBE YAVIN GUWOLE. HSUOKT LAM ZPZKVRN.

Adding letters to it helps figure out the key length. Adding three (IMPERAAA) reveals a slightly more coherent message.

REBEL NOCCES HADE PVADED. I TCACKER PAD BEEN PTANED ON OVE ZF THEIZ SSIPS. THM SNUM APPMAC TO BE IV TSE YAVIV SJSTEM. FWLWOW AND LEDTROY.

From here you can change up the last three letters of the key to build words. This will eventually yield IMPERIAL

Decrypted Message: "REBEL FORCES HAVE EVADED. A TRACKER HAS BEEN PLACED ON ONE OF THEIR SHIPS. THE SCUM APPEAR TO BE IN THE YAVIN SYSTEM. FOLLOW AND DESTROY."

# Operation Fleet Veil (Hard) NOT VETTED ##########################

## Challenge:
 Your determination and expertise have brought forth a new revelation crucial to our cause. In a startling discovery, we have learned that the Empire has devised a tracking cipher to monitor the movements of our precious Rebel fleet. This encryption poses a grave threat to our operations and the safety of our forces. It is imperative that we decrypt the Empire's tracking algorithm and neutralize their surveillance capabilities.

Your mission is to unravel the intricacies of this tracking cipher and decipher the encrypted transmissions intercepted from the Empire. By doing so, we can gain vital information about the Empire's tracking methods and devise countermeasures to protect our fleet.

Prepare to employ your advanced cryptographic skills and algorithmic understanding to break through the Empire's encryption walls. The future of our Rebellion depends on your ability to thwart their tracking efforts and safeguard our fleet from imminent danger.

May the Force guide your every calculation and may your perseverance shine through as you embark on Operation Fleet Veil to secure the survival of our Rebel fleet.

Public Key:
    Modulus (N): 114931
    Public Exponent (e): 17
    
Ciphertext: 54222 24241 82981 22142 22344 2934 102064 60961 64751 2934 60961 2934 11455 19961 60040 22344




## Solution:
To retrieve the flag, follow these steps:
Decrypt each ciphertext separately using the RSA decryption formula: M = C^d mod N, where M is the plaintext (ASCII value of each character), C is the ciphertext, d is the private key, and N is the modulus.
Convert each decrypted ASCII value to its corresponding character.
Concatenate the characters to form the flag.
Your Task:
Decrypt the provided ciphertext using the given public key values and retrieve the flag. Submit the flag "CTF{rsa_is_secure}" as the solution.

### Example Decryption:
Ciphertext: 54222
Decrypted ASCII value: 54222^67571 mod 114931 ≈ 67
Character: 'C'

Ciphertext: 24241
Decrypted ASCII value: 24241^67571 mod 114931 ≈ 84
Character: 'T'

Ciphertext: 82981
Decrypted ASCII value: 82981^67571 mod 114931 ≈ 70
Character: 'F'
...

Submit the flag "CTF{rsa_is_secure}" as the solution to this challenge.


# Polybius Square Encryption (Hard)

## Challenge

You've intercepted a secret message that has been encrypted using a Polybius Square cipher. The message is in the form of a series of numbers, which represent the coordinates of each letter in the Polybius Square grid. Your task is to decrypt the ciphertext and reveal the hidden message.

Ciphertext:
1334332242114445311144343343543445231151154334315115144423151114511133131514134254354434224211352354132311313115332215

Your goal is to create a script that can decrypt the ciphertext by implementing the following steps:

Generate the Polybius Square:
Your script should include a function that generates the Polybius Square grid. The grid consists of a 5x5 matrix, where each cell corresponds to a letter of the alphabet. You should map each letter to its corresponding coordinate in the grid.

Decrypt the Ciphertext:
Write a decryption function that takes the ciphertext and the Polybius Square grid as input. Your function should iterate over each pair of numbers in the ciphertext, convert them into coordinates, and retrieve the corresponding letter from the Polybius Square grid. By building the decrypted plaintext message using the decrypted letters, you can unveil the hidden message.

To solve this challenge, you need to run your script with the given ciphertext and the generated Polybius Square grid as inputs. The script should output the decrypted plaintext message, revealing the secret communication.

Note: The Polybius Square grid is a fundamental part of this encryption algorithm. Make sure to include it in your script and use it for decrypting the ciphertext.

Good luck!


# Solution
To solve the Polybius Square encryption challenge, follow these steps:

Generate the Polybius Square:
Implement a function that generates the Polybius Square grid, mapping each letter of the alphabet to its corresponding coordinate. The grid should be a 5x5 matrix with letters A to E as row headers and column headers.

Example Polybius Square Grid:

  1 2 3 4 5
1 A B C D E
2 F G H I/J K
3 L M N O P
4 Q R S T U
5 V W X Y Z

Decrypt the Ciphertext:
Write a decryption function that takes the ciphertext and the Polybius Square grid as inputs. Iterate over each pair of numbers in the ciphertext and convert them into coordinates.

Example Ciphertext: 231531431122442531151322 141543124414441 33243242 25113525 3441532215 441543124414 445151534 4153544434 352522 4424324425 3243514 231531431122

Split the ciphertext into pairs of numbers: 23 15 31 43 11 22 44 25 31 15 13 22, 14 15 43 12 44 14 41, 33 24 32 42, 25 11 35 25, 34 41 53 22 15, 44 15 43 12 44 14 41, 44 51 51 53 4, 41 53 54 44 34, 35 25 22, 44 24 32 44 25, 32 43 51 4, 23 15 31 43 11 22.

For each pair of numbers, convert them into coordinates using the Polybius Square grid. For example, the pair "23" corresponds to the coordinates (2, 3) in the grid.

Retrieve the corresponding letter from the Polybius Square grid based on the obtained coordinates.

Build the decrypted plaintext message by concatenating the decrypted letters.

Example Decryption:

Pair "23" corresponds to the letter "C".
Pair "15" corresponds to the letter "A".
Pair "31" corresponds to the letter "F".
Pair "43" corresponds to the letter "I/J".
Pair "11" corresponds to the letter "B".
Pair "22" corresponds to the letter "G".
Continue this process for all pairs to obtain the decrypted plaintext message.

Run the Script:
Execute the script you created, which includes the Polybius Square generation and decryption functions. Provide the given ciphertext and the Polybius Square grid as inputs.

The script should output the decrypted plaintext message.

In this specific challenge, the decrypted plaintext message is "CONGRATULATIONS YOU HAVE SOLVED THE ADVANCED CRYPTOGRAPHY CHALLENGE."

Congratulations on successfully decrypting the Polybius Square ciphertext and completing the challenge!

### Script:
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
