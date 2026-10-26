from business_rules import (
    calculate_bean_cost,
    calculate_shipment_total,
    format_shipment_line,
    get_bulk_discount,
    largest_shipment,
    needs_pallet,
    requires_prepayment,
    total_shipped,
)


def test_bean_cost():
    assert calculate_bean_cost(12.0, 5) == 60.0


def test_discount_below_20():
    assert get_bulk_discount(19) == 0.0


def test_discount_at_20():
    assert get_bulk_discount(20) == 0.09


def test_discount_at_79():
    assert get_bulk_discount(79) == 0.09


def test_discount_at_80():
    assert get_bulk_discount(80) == 0.14


def test_partner_discount():
    assert round(get_bulk_discount(20, True), 2) == 0.13


def test_prepayment_limit():
    assert requires_prepayment(1500.0) is True


def test_pallet_conditions():
    assert needs_pallet(61, 701.0) is True


def test_bean_cost_zero():
    assert calculate_bean_cost(15.0, 0) == 0.0


def test_partner_below_20():
    assert get_bulk_discount(10, True) == 0.0


def test_partner_at_80():
    assert round(get_bulk_discount(80, True), 2) == 0.18


def test_shippimg_below_250():
    assert round(calculate_shipment_total(24.90, 10), 2) == 284.00


def test_shipping_at_250():
    assert calculate_shipment_total(25.0, 10) == 250.0


def test_discounted_shipment_at_20():
    assert round(calculate_shipment_total(10.0, 20), 2) == 217.0


def test_prepayment_below_1500():
    assert requires_prepayment(1499.99) is False


def test_prepayment_above_1500():
    assert requires_prepayment(1500.01) is True


def test_pallet_exactly_60_bags():
    assert needs_pallet(60, 701.0) is False


def test_pallet_exactly_700():
    assert needs_pallet(61, 700.0) is False


def test_pallet_below_60():
    assert needs_pallet(59, 701.0) is False


def test_total_shipped_two_orders():
    orders = [
        {"buyer": "A", "bag_price": 10.0, "bags": 10, "partner": False},
        {"buyer": "B", "bag_price": 20.0, "bags": 10, "partner": False},
    ]
    assert round(total_shipped(orders), 2) == 370.0


def test_total_shipped_empty():
    assert total_shipped([]) == 0.0


def test_largest_shipment_second():
    orders = [
        {"buyer": "A", "bag_price": 10.0, "bags": 10, "partner": False},
        {"buyer": "B", "bag_price": 30.0, "bags": 10, "partner": False},
    ]
    assert largest_shipment(orders) == "B"


def test_largest_shipment_tie():
    orders = [
        {"buyer": "A", "bag_price": 10.0, "bags": 10, "partner": False},
        {"buyer": "B", "bag_price": 10.0, "bags": 10, "partner": False},
    ]
    assert largest_shipment(orders) == "A"


def test_largest_shipment_empty():
    assert largest_shipment([]) == ""


def test_format_shipment_np():
    result = format_shipment_line("Bakery", 175.0, False, False)
    assert result == "Bakery: $175.00 | prepayment: no | pallet: no"


def test_format_shipment_yes():
    result = format_shipment_line("Hotel", 1500.0, True, True)
    assert result == "Hotel: $1500.00 | prepayment: yes | pallet: yes"
