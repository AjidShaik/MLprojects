# Program to add two numbers entered by the user

def add_numbers(a, b):
    return a + b

def main():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = add_numbers(num1, num2)
        print(f"The sum of {num1} and {num2} is {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()

