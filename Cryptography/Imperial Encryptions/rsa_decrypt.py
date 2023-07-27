import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_phi(p, q):
    return (p - 1) * (q - 1)

def modular_inverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return None

def decrypt_rsa(ciphertext, modulus, private_exponent):
    decrypted_message = ""
    for num in ciphertext:
        decrypted_num = pow(num, private_exponent, modulus)
        decrypted_message += chr(decrypted_num)
    return decrypted_message

# Public key parameters
modulus = 114931
public_exponent = 17

# Ciphertext
ciphertext = [54222, 24241, 82981, 22142, 22344, 2934, 102064, 60961, 64751, 2934, 60961, 2934, 11455, 19961, 60040, 22344]

# Brute force the possible values of p and q
for p in range(2, int(math.sqrt(modulus)) + 1):
    if modulus % p == 0:
        q = modulus // p
        phi = find_phi(p, q)
        if gcd(public_exponent, phi) == 1:
            private_exponent = modular_inverse(public_exponent, phi)
            if private_exponent is not None:
                decrypted_message = decrypt_rsa(ciphertext, modulus, private_exponent)
                break

print("Decrypted message:", decrypted_message)
