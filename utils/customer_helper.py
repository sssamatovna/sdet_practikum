from typing import List

def find_customer_delete(customer_names: List[str]) -> str:
    if not customer_names:
        return ""
    lengths = [len(n) for n in customer_names]
    avg = sum(lengths) / len(lengths)
    best_idx = min(range(len(customer_names)), key=lambda i: abs(len(customer_names[i]) - avg))
    return customer_names[best_idx]