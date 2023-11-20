
from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)

f = Fernet(key)

original = b"A really secret message. Not for prying eyes."
print(original)

encrypted = f.encrypt(original)
print(encrypted)

decrypted = f.decrypt(encrypted)
print(decrypted)





