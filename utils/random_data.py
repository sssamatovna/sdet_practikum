import random
import math


def generate_post_code() -> str:
    """Генерирует 10-значный почтовый индекс."""
    return str(random.randint(1000000000, 9999999999))


def generate_first_name(post_code: str) -> str:
    """Генерирует First Name (длина 5) на основе Post Code."""
    if len(post_code) != 10:
        raise ValueError("Post Code должен состоять из 10 цифр")

    name_chars = []
    pairs = [post_code[i:i + 2] for i in range(0, 10, 2)]

    for pair in pairs:
        value = int(pair)
        letter_index = value % 26
        letter = chr(ord('a') + letter_index)
        name_chars.append(letter)

    return "".join(name_chars)


# >>> НОВАЯ ФУНКЦИЯ: Генерация имени заданной длины
def generate_name_by_length(length: int) -> str:
    """
    Генерирует случайное имя заданной длины (из случайных букв).

    Для этой задачи мы используем простой способ, так как генерация
    пост-кода с нужной длиной имени (кроме 5) очень сложна.
    """
    # 97 - ASCII код 'a', 122 - ASCII код 'z'
    return "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=length)).capitalize()