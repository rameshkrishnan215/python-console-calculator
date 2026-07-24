import math

while True:
    print("\n===== CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square Root")
    print("8. Percentage")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "9":
        print("See you later!")
        break

    elif choice == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Answer:", num1 + num2)

    elif choice == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Answer:", num1 - num2)

    elif choice == "3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Answer:", num1 * num2)

    elif choice == "4":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 != 0:
            print("Answer:", num1 / num2)
        else:
            print("Cannot divide by zero.")

    elif choice == "5":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 != 0:
            print("Answer:", num1 % num2)
        else:
            print("Cannot perform modulus with zero.")

    elif choice == "6":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Answer:", num1 ** num2)

    elif choice == "7":
        num = float(input("Enter a number: "))
        if num >= 0:
            print("Answer:", math.sqrt(num))
        else:
            print("Square root of a negative number is not possible.")

    elif choice == "8":
        number = float(input("Enter a number: "))
        percentage = float(input("Enter percentage: "))
        print("Answer:", (number * percentage) / 100)

    else:
        print("Invalid choice. Please enter a number between 1 and 9.")
