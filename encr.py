import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding, default_backend

# Generate a random key of the appropriate length for the chosen encryption algorithm
key = os.urandom(32)

def encrypt(data, key):
    # Create a Cipher object using the chosen encryption algorithm and mode
    cipher = Cipher(algorithms.AES(key), modes.CTR(b'\x00' * 16), backend=default_backend())
    
    # Create an encryptor object using the Cipher object
    encryptor = cipher.encryptor()
    
    # Pad the data to be encrypted to the appropriate block size
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    
    # Encrypt the padded data using the encryptor object
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    
    # Return the encrypted data as a string of characters
    return encrypted_data.hex()

def decrypt(encrypted_data, key):
    # Convert the encrypted data string back into bytes
    encrypted_data_bytes = bytes.fromhex(encrypted_data)
    
    # Create a Cipher object using the chosen encryption algorithm and mode
    cipher = Cipher(algorithms.AES(key), modes.CTR(b'\x00' * 16), backend=default_backend())
    
    # Create a decryptor object
