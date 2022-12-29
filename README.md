# Encryptor
This code uses the Fernet module from the cryptography library to encrypt and decrypt data using the AES algorithm.

First, it imports the necessary libraries and generates a random password for the key using the Fernet.generate_key() method.

Then, it derives a key from the password using the PBKDF2 key derivation function (KDF) with the SHA256 hashing algorithm, a salt value, and 100000 iterations. The key is then encoded using base64 for safe storage or transmission.

Next, it creates a Fernet object using the key and uses it to encrypt some data. The encrypted data is then decrypted and the results are printed to the console. Finally, the script verifies that the decrypted data is the same as the original data by using an assertion.
