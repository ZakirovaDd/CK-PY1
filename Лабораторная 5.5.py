from random import sample
from string import ascii_lowercase, ascii_uppercase, digits
def get_random_password() -> str:
    symbol = digits + ascii_lowercase + ascii_uppercase
    return ''.join(sample(symbol, 8))

print(get_random_password())
