from Crypto.Hash import SHA1

# SHA1:
# Documentation: https://pycryptodome.readthedocs.io/en/latest/src/hash/sha1.html


def encrypt_sha1(word):
    try:
        h = SHA1.new()
        # The input parameter is converted into bytes.
        h.update(bytes(word, 'utf-8'))
        return h.hexdigest()
    except TypeError:
        return "Enter a string"
