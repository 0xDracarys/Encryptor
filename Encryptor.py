import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Generate a random password for the key
password = Fernet.generate_key()

# Derive a key from the password using PBKDF2
salt = b'salt_'  # Prefix the salt with "salt_" to ensure it is a valid salt
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000
)
key = base64.urlsafe_b64encode(kdf.derive(password))

# Create a Fernet object using the key
fernet = Fernet(key)

# Encrypt some data
data = b'This is some sensitive data'
encrypted_data = fernet.encrypt(data)

# Decrypt the data
decrypted_data = fernet.decrypt(encrypted_data)

# Print the results
print(f'Original data: {data}')
print(f'Encrypted data: {encrypted_data}')
print(f'Decrypted data: {decrypted_data}')

# Verify that the decrypted data is the same as the original data
assert decrypted_data == data
