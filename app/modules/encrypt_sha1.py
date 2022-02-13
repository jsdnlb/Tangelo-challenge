from Crypto.Hash import SHA1
from app.modules.error_messages import error_messages

# SHA1:
# Documentation: https://pycryptodome.readthedocs.io/en/latest/src/hash/sha1.html


def encrypt_sha1(word):
    try:
        h = SHA1.new()
        # The input parameter is converted into bytes.
        h.update(bytes(word, 'utf-8'))
        return h.hexdigest()
    except TypeError:
        return error_messages('MSG_TYPE_ERROR')
