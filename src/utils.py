def calculate_percentage_change(old_price: float, new_price: float) -> float:
    """Calculates the percentage change between two price marks safely."""
    if old_price <= 0:
        return 0.0
    return round(((new_price - old_price) / old_price) * 100, 2)
