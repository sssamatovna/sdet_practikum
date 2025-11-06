import random
import string

def generate_customer_data(name_length: int = 5) -> tuple[str, str]:
    post_code_length = name_length * 2  # по заданию 10 цифр при name_length=5
    post_code = "".join(random.choices(string.digits, k=post_code_length))

    alphabet = string.ascii_lowercase
    first_name_chars = []
    for i in range(0, post_code_length, 2):
        n = int(post_code[i:i+2])
        first_name_chars.append(alphabet[n % 26])
    first_name = "".join(first_name_chars).capitalize()
    return first_name, post_code