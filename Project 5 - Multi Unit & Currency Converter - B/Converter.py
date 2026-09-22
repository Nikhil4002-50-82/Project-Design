# Task 1 - Create the entry file and print welcome header
# Step 1: Entry File Setup
def print_welcome():
    # Step 2: Welcome Banner Output
    print("Welcome to Multi-Unit & Currency Converter CLI!")


# Task 2 - Define Currency rates table (Base: USD)
# Step 1: Declare Currency Rates Lookup Table
CURRENCY_RATES = {
    "USD": 1.0,
    "EUR": 0.92,
    "GBP": 0.79,
    "INR": 83.0,
    "JPY": 155.0,
    "CAD": 1.36
}


# Task 3 - Implement Currency conversion function
def convert_currency(amount, from_unit, to_unit):
    # Step 1: Pivot Input Amount to Standard Base (USD)
    amount_in_usd = amount / CURRENCY_RATES[from_unit]

    # Step 2: Project Base Amount to Target Currency
    return amount_in_usd * CURRENCY_RATES[to_unit]


# Task 4 - Define Length conversion ratios (Base: Meters)
# Step 1: Declare Length Ratios Lookup Table
LENGTH_RATIOS = {
    "m": 1.0,
    "km": 1000.0,
    "mi": 1609.344,
    "ft": 0.3048,
    "in": 0.0254
}


# Task 5 - Implement Length conversion function
def convert_length(amount, from_unit, to_unit):
    # Step 1: Normalize Distance to Base Metric (Meters)
    amount_in_meters = amount * LENGTH_RATIOS[from_unit]

    # Step 2: Project Base Distance to Target Unit
    return amount_in_meters / LENGTH_RATIOS[to_unit]


# Task 6 - Define Weight conversion ratios (Base: Kilograms)
# Step 1: Declare Weight Ratios Lookup Table
WEIGHT_RATIOS = {
    "kg": 1.0,
    "g": 0.001,
    "lbs": 0.45359237,
    "oz": 0.028349523125
}


# Task 7 - Implement Weight conversion function
def convert_weight(amount, from_unit, to_unit):
    # Step 1: Normalize Mass to Base Metric (Kilograms)
    amount_in_kg = amount * WEIGHT_RATIOS[from_unit]

    # Step 2: Project Base Mass to Target Unit
    return amount_in_kg / WEIGHT_RATIOS[to_unit]


# Task 8 - Implement Temperature conversion function (Base: Celsius)
def is_below_absolute_zero(amount, unit):
    # Step 1: Validate Absolute Zero Physical Boundary
    if unit == "C" and amount < -273.15:
        return True
    if unit == "F" and amount < -459.67:
        return True
    if unit == "K" and amount < 0.0:
        return True
    return False


def convert_temperature(amount, from_unit, to_unit):
    # Step 2: Convert Input Scale to Base Celsius
    if from_unit == "C":
        celsius = amount
    elif from_unit == "F":
        celsius = (amount - 32.0) * 5.0 / 9.0
    elif from_unit == "K":
        celsius = amount - 273.15
    else:
        return 0.0

    # Step 3: Project Base Celsius to Target Scale
    if to_unit == "C":
        return celsius
    elif to_unit == "F":
        return (celsius * 9.0 / 5.0) + 32.0
    elif to_unit == "K":
        return celsius + 273.15
    return 0.0


# Task 9 - Validate numeric input
def get_positive_number(prompt):
    # Step 1: Read and Validate Non-Negative Number
    while True:
        raw = input(prompt).strip()
        try:
            val = float(raw)
            if val < 0:
                print("Error: Amount cannot be negative. Please enter a positive value.")
                continue
            return val
        except ValueError:
            print("Error: Invalid numeric input. Please enter a valid number.")


def get_temperature_number(prompt, unit):
    # Step 2: Read and Validate Bounded Temperature
    while True:
        raw = input(prompt).strip()
        try:
            val = float(raw)
            if is_below_absolute_zero(val, unit):
                print(f"Error: Temperature cannot be below Absolute Zero ({val} {unit}).")
                continue
            return val
        except ValueError:
            print("Error: Invalid numeric input. Please enter a valid number.")


# Task 10 - Validate unit selections
def get_valid_unit(prompt, allowed_units):
    # Step 1: Normalize Case and Match Against Allowed Units
    while True:
        user_input = input(prompt).strip()
        for original in allowed_units:
            if user_input.lower() == original.lower():
                return original
        print(f"Error: Invalid unit '{user_input}'. Allowed options: {', '.join(allowed_units)}")


# Task 11 - Build interactive conversion handlers
def handle_currency():
    # Step 1: Build Currency Conversion Handler
    print("\n--- CURRENCY CONVERTER ---")
    units = list(CURRENCY_RATES.keys())
    print(f"Supported Currencies: {', '.join(units)}")
    from_curr = get_valid_unit("Enter Source Currency: ", units)
    to_curr = get_valid_unit("Enter Target Currency: ", units)
    amount = get_positive_number(f"Enter amount in {from_curr}: ")

    result = convert_currency(amount, from_curr, to_curr)
    rate = convert_currency(1.0, from_curr, to_curr)
    print(f"\n>> RESULT: {amount:.2f} {from_curr} = {result:.2f} {to_curr}")
    print(f"   (Exchange Rate: 1 {from_curr} = {rate:.4f} {to_curr})")


def handle_length():
    # Step 2: Build Length Conversion Handler
    print("\n--- LENGTH CONVERTER ---")
    units = list(LENGTH_RATIOS.keys())
    print(f"Supported Units: {', '.join(units)} (m=meters, km=kilometers, mi=miles, ft=feet, in=inches)")
    from_u = get_valid_unit("Enter Source Unit: ", units)
    to_u = get_valid_unit("Enter Target Unit: ", units)
    amount = get_positive_number(f"Enter distance in {from_u}: ")

    result = convert_length(amount, from_u, to_u)
    rate = convert_length(1.0, from_u, to_u)
    print(f"\n>> RESULT: {amount:.4f} {from_u} = {result:.4f} {to_u}")
    print(f"   (Ratio: 1 {from_u} = {rate:.4f} {to_u})")


def handle_weight():
    # Step 3: Build Weight Conversion Handler
    print("\n--- WEIGHT CONVERTER ---")
    units = list(WEIGHT_RATIOS.keys())
    print(f"Supported Units: {', '.join(units)} (kg=kilograms, g=grams, lbs=pounds, oz=ounces)")
    from_u = get_valid_unit("Enter Source Unit: ", units)
    to_u = get_valid_unit("Enter Target Unit: ", units)
    amount = get_positive_number(f"Enter weight in {from_u}: ")

    result = convert_weight(amount, from_u, to_u)
    rate = convert_weight(1.0, from_u, to_u)
    print(f"\n>> RESULT: {amount:.4f} {from_u} = {result:.4f} {to_u}")
    print(f"   (Ratio: 1 {from_u} = {rate:.4f} {to_u})")


def handle_temperature():
    # Step 4: Build Temperature Conversion Handler
    print("\n--- TEMPERATURE CONVERTER ---")
    units = ["C", "F", "K"]
    print(f"Supported Scales: {', '.join(units)} (C=Celsius, F=Fahrenheit, K=Kelvin)")
    from_u = get_valid_unit("Enter Source Scale: ", units)
    to_u = get_valid_unit("Enter Target Scale: ", units)
    amount = get_temperature_number(f"Enter temperature in {from_u}: ", from_u)

    result = convert_temperature(amount, from_u, to_u)
    print(f"\n>> RESULT: {amount:.2f} {from_u} = {result:.2f} {to_u}")


# Task 12 - Implement main menu loop and application assembly
def main():
    print_welcome()
    while True:
        # Step 1: Render Interactive Menu Banner
        print("\n========================================")
        print("   MULTI-UNIT & CURRENCY CONVERTER CLI   ")
        print("========================================")
        print("1. Currency Converter (USD, EUR, GBP, INR, JPY, CAD)")
        print("2. Length Converter (m, km, mi, ft, in)")
        print("3. Weight Converter (kg, g, lbs, oz)")
        print("4. Temperature Converter (C, F, K)")
        print("5. Exit")
        print("----------------------------------------")

        # Step 2: Prompt and Route User Selection
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            handle_currency()
        elif choice == "2":
            handle_length()
        elif choice == "3":
            handle_weight()
        elif choice == "4":
            handle_temperature()
        elif choice == "5":
            # Step 3: Handle Exit and Farewell
            print("\nThank you for using Multi-Unit & Currency Converter CLI. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


# Step 4: Assemble Main Entry Point Guard
if __name__ == "__main__":
    main()
