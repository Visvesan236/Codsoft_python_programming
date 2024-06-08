def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

def get_operation_choice():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    while True:
        choice = input("Enter choice (1/2/3/4): ")
        if choice in ['1', '2', '3', '4']:
            return choice
        else:
            print("Invalid choice. Please select a valid operation (1/2/3/4).")

def get_numbers():
    while True:
        try:
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
            return number1, number2
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def calculator():
    print("Welcome to the Calculator!")
    while True:
        operation = get_operation_choice()
        number1, number2 = get_numbers()

        if operation == '1':
            result = add(number1, number2)
            print(f"The result of {number1} + {number2} is: {result:.2f}")

        elif operation == '2':
            result = subtract(number1, number2)
            print(f"The result of {number1} - {number2} is: {result:.2f}")

        elif operation == '3':
            result = multiply(number1, number2)
            print(f"The result of {number1} * {number2} is: {result:.2f}")

        elif operation == '4':
            result = divide(number1, number2)
            if isinstance(result, str):
                print(result)
            else:
                print(f"The result of {number1} / {number2} is: {result:.2f}")

        another_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if another_calculation.lower() != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

calculator()
