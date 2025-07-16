while True:
    try:
        num1 = float(input("Enter the first number: "))
        operation = input("Enter operation (+, -, *, /, %): ")
        num2 = float(input("Enter the second number: "))

        if operation == '+':
            result = num1 + num2
            symbol = '+'
        elif operation == '-':
            result = num1 - num2
            symbol = '-'
        elif operation == '*':
            result = num1 * num2
            symbol = '*'
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.\n")
                continue
            result = num1 / num2
            symbol = '/'
        elif operation == '%':
            if num2 == 0:
                print("Error: Modulus by zero is not allowed.\n")
                continue
            result = num1 % num2
            symbol = '%'
        else:
            print("Invalid operation choice.\n")
            continue

        print(f"Result: {num1} {symbol} {num2} = {result}\n")

    except ValueError:
        print("Invalid input. Please enter numeric values.\n")
