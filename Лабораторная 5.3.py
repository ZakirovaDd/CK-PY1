from random import randint
def get_unique_list_numbers() -> list[int]:
    count = 15
    return [randint(-10, 10) for _ in range(count)]

print(get_unique_list_numbers())