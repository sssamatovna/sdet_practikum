from typing import List, Optional
import math
import allure


@allure.step("Выбрать клиента для удаления по среднему арифметическому")
def find_customer_delete(customer_names: list[str]) -> str:

    if not customer_names:
        return ""
    name_lengths = [len(name) for name in customer_names]
    average_lengths = sum(name_lengths) / len(name_lengths)
    closet_name = min(customer_names, key=lambda name: abs(len(name) - average_lengths))
    return closet_name