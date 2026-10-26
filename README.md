# ISM3232 Midterm: Copper Kettle Coffee Roasters

- **Name:** Aigerim Valiyeva
- **Version:** ZETA
- **Date:** October 25, 2026

## What This Program Does
This Python program creates a shipment report for Copper Kettle Coffee Roasters. It calculates coffee costs, applies quantity and partner discounts, and adds shipping fees if needed. It also checks prepayment and palet requirements and displays a summary of eight shipments.
## Business Rules
1. Bean cost = price per bag * number of bags.
2. Discounts: under 20 bags = 0%; 20-79 = 9%; 80+ = 14%.
3. Partner cafes get 4 extra percentage points of discount on orders of 20+ bags.
4. Add $35 shipping if the discounted cost is below $250.
5. Shipments of $1,500 or more require prepayment.
6. A pallet is required for more than 60 bags and a shipment total over $700.
## How to Run
Open the terminal in the project folder and run:
```bash 
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py
```
## How to Test
Run the following commands:
```bash
ruff format --check .
ruff check .
pytest -v
```
The project includes 26 pytest tests covering the 8 business functions and their boundary conditions.
## Files in This Repository
- `business_rules.py` - Contains the 8 business rule functions.
- `main.py` - Contains shipment data and prints the shipment report.
- `commands.md` - Records terminal commands, output, and project verification.
- `README.md` - Explains the project and how to run it.
- `requirements.txt` - Lists the Python dependencies.
- `.gitignore` - Excludes virtual environments, caches, and generated files.
- `tests/__init__.py` - Identifies the tests package.
- `tests/test_business_rules.py` - Contains the 26 pytest tests.
## AI Use Statement
I did not use any AI tools or assistance while completing this exam.