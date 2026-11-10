
# =====================================
# SIMON'S OHM'S LAW AND POWER CALCULATOR
# Author: Simon
# Department: Mechatronics Engineering
# =====================================

# This list stores previous calculations
history = []


# Function to calculate voltage
def calculate_voltage():
    current = float(input("Enter current (Amperes): "))
    resistance = float(input("Enter resistance (Ohms): "))

    voltage = current * resistance
    result = f"Voltage = {voltage} Volts"

    print(result)
    history.append(result)


# Function to calculate current
def calculate_current():
    voltage = float(input("Enter voltage (Volts): "))
    resistance = float(input("Enter resistance (Ohms): "))

    if resistance == 0:
        print("Error: Resistance cannot be zero")
    else:
        current = voltage / resistance
        result = f"Current = {current} Amperes"
        print(result)
        history.append(result)


# Function to calculate resistance
def calculate_resistance():
    voltage = float(input("Enter voltage (Volts): "))
    current = float(input("Enter current (Amperes): "))

    if current == 0:
        print("Error: Current cannot be zero")
    else:
        resistance = voltage / current
        result = f"Resistance = {resistance} Ohms"
        print(result)
        history.append(result)


# Function to calculate electrical power
def calculate_power():
    voltage = float(input("Enter voltage (Volts): "))
    current = float(input("Enter current (Amperes): "))

    power = voltage * current
    result = f"Power = {power} Watts"

    print(result)
    history.append(result)


# Main program menu
while True:

    print("\n===== SIMON'S CALCULATOR =====")
    print("1. Calculate Voltage")
    print("2. Calculate Current")
    print("3. Calculate Resistance")
    print("4. Calculate Power")
    print("5. View Calculation History")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    # Handle invalid numerical inputs
    try:

        if choice == "1":
            calculate_voltage()

        elif choice == "2":
            calculate_current()

        elif choice == "3":
            calculate_resistance()

        elif choice == "4":
            calculate_power()

        elif choice == "5":

            print("\nCalculation History:")

            if len(history) == 0:
                print("No calculations yet.")
            else:
                for item in history:
                    print(item)

        elif choice == "6":
            print("Thank you for using Simon's Calculator!")
            break

        else:
            print("Invalid choice. Please try again.")

    except ValueError:
        print("Error: Please enter numbers only.")
