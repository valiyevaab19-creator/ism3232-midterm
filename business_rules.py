MIN_DISCOUNT_BAGS = 20
LARGE_DISCOUNT_BAGS = 80
REGULAR_DISCOUNT = 0.09
LARGE_DISCOUNT = 0.14
PARTNER_EXTRA_DISCOUNT = 0.04
NO_DISCOUNT = 0.0
SHIPPING_FEE = 35.0
SHIPPING_THRESHOLD = 250.0
PREPAYMENT_THRESHOLD = 1500.0
PALLET_BAG_THRESHOLD = 60
PALLET_TOTAL_THRESHOLD = 700.0

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
def calculate_shipment_total(
          bag_price: float, bags: int, partner: bool = False
) -> float:
     """Calculate the total shipment cost after discount and shipping."""
     cost = calculate_bean_cost(bag_price, bags)
     discount = get_bulk_discount(bags, partner)
     total = cost * (1 - discount)

     if total < SHIPPING_THRESHOLD:
          total += SHIPPING_FEE

     return total
    
    
def requires_prepayment(total: float) -> bool:
    """Return whether a shipment requires prepayment."""
    return total >= PREPAYMENT_THRESHOLD

def needs_pallet(bags: int, total: float) -> bool:
    """Return whether a shipment needs a freight pallet."""
    return bags > PALLET_BAG_THRESHOLD and total > PALLET_TOTAL_THRESHOLD