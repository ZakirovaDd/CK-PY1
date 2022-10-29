from random import sample
from string import ascii_lowercase, ascii_uppercase, digits
def get_random_password() -> str:
    symbols = digits + ascii_lowercase + ascii_uppercase
    lenght_of_password = 8
    return ''.join(sample(symbols, lenght_of_password))

print(get_random_password())

