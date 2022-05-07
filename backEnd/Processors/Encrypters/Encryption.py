
# Importing Builtin Libraries
import sys
from cryptography.fernet import Fernet
# Importing User defined Modules
from backEnd.propertyFiles.EnvironmentVariables import decreptionKey

# pathToDecryptionKey = "../SecretFiles/decryptionKey.key"

# def write_key():
#     """
#     Generates a key and save it into a file
#     """
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)

# LOAD KEY
def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    # return open(pathToDecryptionKey, "rb").read()
    return decreptionKey

# ENCRYPT PII COLOUMN VALUE
def encrypt(coloumnValue, key):
    EncodedData = coloumnValue.encode()
    fernetObject = Fernet(key)
    # encrypt data
    encrypted_data = fernetObject.encrypt(EncodedData)

    return encrypted_data.decode()

# DECRYPT PII COULOMN VALUE
def decrypt(encryptedData,key):
    fernetObject = Fernet(key)

    # decrypt data
    decrypted_data = fernetObject.decrypt(encryptedData)

    return decrypted_data

# CALL THIS FUNCTION WHILE DECODING STRING
def wrapperDecyptFunction(encryptedData):
    encryptedEncodedData = encryptedData.encode()

    # LOAD ENCRYPTION-DECRYPTION KEY
    Key = load_key()

    # DECRYPT PASSWORD TO OPEN SQL CONNECTION
    decryptedString = decrypt(encryptedEncodedData,Key)

    # FUNCTION DECRYPT RETURNS A ENCODED STRING, WE HAVE TO DECODE IT TO ACCESS
    return decryptedString.decode()

# CALL THIS FUNCTION WHILE ENCODING STRING
def wrapperEncryptFunction(coloumnValue):
    # LOAD ENCRYPTION-DECRYPTION KEY
    Key = load_key()

    # DECRYPT PASSWORD TO OPEN SQL CONNECTION
    encryptedString = encrypt(coloumnValue,Key)

    return encryptedString
