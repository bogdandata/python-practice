def main():
    print("Welcome to the calculator!")
    while True:
        print("Please select an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            result = num1 + num2
            print(f"The result of {num1} + {num2} is: {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"The result of {num1} - {num2} is: {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"The result of {num1} * {num2} is: {result}")
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is: {result}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()