# Terminal Record: Copper Kettle Coffee Roasters

## 1. Building the project
```bash
cd ~/Desktop
mkdir -p ism3232-midterm
cd ism3232-midterm
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install pytest ruff
mkdir -p tests
touch business_rules.py
touch main.py
touch commands.md
touch README.md
touch tests/__init__.py
touch tests/test__business_rules.py
printf '.venv/\n__pycache__/\n.pytest_cache/\n.ruff_cache/\n*.pyc\n' > .gitignore
python3 -m pip freeze > requirements.txt
git init -b main
git add .
git commit -m "Create initial midterm project structure"
git remote add origin https://github.com/valiyevaab19-creator/ism3232-midterm
git push -u origin main
```
## 2. The virtual environment
```bash
which python3
```
```text
/Users/aigerimvaliyeva/Desktop/ism3232-midterm/.venv/bin/python3

```
The output shows that Python is running from the project's virtual environment.
## 3. The project structure
```bash
tree -L 2
```

```text
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-313.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files

```
The .venv folder is on my computer but not on GitHub because it is excluded by .gitignore.
## 4. Every function and test
```bash
rg 'def ' -g '*.py'
```
```text
business_rules.py:def calculate_bean_cost(bag_price: float, bags: int) -> float:
business_rules.py:def get_bulk_discount(bags: int, partner: bool = False) -> float:
business_rules.py:def calculate_shipment_total(
business_rules.py:def requires_prepayment(total: float) -> bool:
business_rules.py:def needs_pallet(bags: int, total: float) -> bool:
business_rules.py:def total_shipped(shipments: list) -> float:
business_rules.py:def largest_shipment(shipments: list) -> str:
business_rules.py:def format_shipment_line(
tests/test_business_rules.py:def test_bean_cost():
tests/test_business_rules.py:def test_discount_below_20():
tests/test_business_rules.py:def test_discount_at_20():
tests/test_business_rules.py:def test_discount_at_79():
tests/test_business_rules.py:def test_discount_at_80():
tests/test_business_rules.py:def test_partner_discount():
tests/test_business_rules.py:def test_prepayment_limit():
tests/test_business_rules.py:def test_pallet_conditions():
tests/test_business_rules.py:def test_bean_cost_zero():
tests/test_business_rules.py:def test_partner_below_20():
tests/test_business_rules.py:def test_partner_at_80():
tests/test_business_rules.py:def test_shippimg_below_250():
tests/test_business_rules.py:def test_shipping_at_250():
tests/test_business_rules.py:def test_discounted_shipment_at_20():
tests/test_business_rules.py:def test_prepayment_below_1500():
tests/test_business_rules.py:def test_prepayment_above_1500():
tests/test_business_rules.py:def test_pallet_exactly_60_bags():
tests/test_business_rules.py:def test_pallet_exactly_700():
tests/test_business_rules.py:def test_pallet_below_60():
tests/test_business_rules.py:def test_total_shipped_two_orders():
tests/test_business_rules.py:def test_total_shipped_empty():
tests/test_business_rules.py:def test_largest_shipment_second():
tests/test_business_rules.py:def test_largest_shipment_tie():
tests/test_business_rules.py:def test_largest_shipment_empty():
tests/test_business_rules.py:def test_format_shipment_np():
tests/test_business_rules.py:def test_format_shipment_yes():

```
The project contains 8 business functions and 26 tests.

## 5. Which files print
```bash 
rg -l 'print' -g '*.py'
```

```text
main.py
```

main.py prints the shipment report. business_rules.py only returns values.

## 6. The commit history
```bash
git log --oneline
```bash
git log --oneline
```

```text
b17bc50 Add comprehensive tests for business rules
6f842da Correct business rules implementation
61c156e Add shipment report and summary
122e174 Implement shipment summaries and formatting
029fbc2 Add shipment calculations and conditions
6588bcc Implement bean cost and bulk discounts
5490624 Create initial midterm project structure

```
There were 7 commits at the time of this check.