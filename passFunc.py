from cryptography.fernet import Fernet
"""
This is a function that will decrypt a stored password.
This key file and passwword storage file are network API
"""
def decryptPass():
    file = open('store.txt', 'rb')
    enc = file.read()
    file.close()

    # Retrive key from file
    # Load Key
    file = open('key.key', 'rb')
    key = file.read() # The key will be type bytes
    file.close()

    # Decrypt password
    f = Fernet(key)
    dec = f.decrypt(enc).decode('utf8')
    return dec

# Create Key
# key = Fernet.generate_key()
#
# # Store Key
# file = open('key.key', 'wb')
# file.write(key) # The key is type bytes still
# file.close()
#
# # Load Key
# file = open('key.key', 'rb')
# key = file.read() # The key will be type bytes
# file.close()
#
# # Use Key
#
# f = Fernet(key)
# # For test purpose, enter password
# password = input("Enter Password: ").encode()
#
# encrypted = f.encrypt(password)
#
# # Store encrypted password in text file
#
# store_pass = open('store.txt', 'wb')
# store_pass.write(encrypted)
# store_pass.close()
#
# # Retrive Encrypted password from file
#
# file = open('store.txt', 'rb')
# enc = file.read()
# file.close()
#
# # Retrive key from file
# # Load Key
# file = open('key.key', 'rb')
# key = file.read() # The key will be type bytes
# file.close()
#
# # Decrypt password
# f = Fernet(key)
# dec = f.decrypt(enc).decode('utf8')
