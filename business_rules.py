MIN_DISCOUNT_BAGS = 20
LARGE_DISCOUNT_BAGS = 80
REGULAR_DISCOUNT = 0.09
LARGE_DISCOUNT = 0.14
PARTNER_EXTRA_DISCOUNT = 0.04
NO_DISCOUNT = 0.0

def calculate_bean_cost(bag_price: float, bags: int) -> float:
    """Calculate the bean cost before discounts."""
    return bag_price * bags

def get_bulk_discount(bags: int, partner: bool = False) -> float:
    """Return the discount rate for the shipment."""
    if bags < MIN_DISCOUNT_BAGS:
        return NO_DISCOUNT

    if bags < LARGE_DISCOUNT_BAGS:
        discount = REGULAR_DISCOUNT
    else: 
        discount = LARGE_DISCOUNT

    if partner:
        discount += PARTNER_EXTRA_DISCOUNT

    return discount