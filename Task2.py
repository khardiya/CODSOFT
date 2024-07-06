def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def main():
    while True:
        print("\nSimple Calculator")

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            print("Select operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")

            choice = input("Enter choice (1/2/3/4): ")

            if choice == '1':
                print(f"The result is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == '4':
                try:
                    print(f"The result is: {divide(num1, num2)}")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("Invalid input")

            continue_choice = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
            if continue_choice not in ('yes', 'y'):
                print("Exiting the calculator. Goodbye!")
                break

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
