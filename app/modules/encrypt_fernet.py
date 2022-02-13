""" Proposal for improvement

SHA1 encryption is not recommended for new designs, even in its own page it says so,
I was investigating new methods and I found Fernet (symmetric encryption):
Fernet guarantees that an encrypted message cannot be manipulated or read without the key. """

from cryptography.fernet import Fernet
from app.modules.error_messages import error_messages


# Fernet (symmetric encryption)
# Documentation: https://cryptography.io/en/latest/fernet/


def encrypt_fernet(word):
    try:

       # Generate a key
        key = Fernet.generate_key()

        # Create the Fernet instance
        # Parameters: key: generated key
        f = Fernet(key)
        # Use the "encrypt" method, but first encode from string to byte
        token = f.encrypt(str.encode(word))
        return token
        
    except TypeError:
        return error_messages('MSG_TYPE_ERROR')
