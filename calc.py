from calculator import add, subtract, multiply, divide, square_root, exponentiate

def main():
    try:
        a = safe_input("Enter the first number: ")
        b = safe_input("Enter the second number: ")
        print("Addition:", add(a, b))
        print("Subtraction:", subtract(a, b))
        print("Multiplication:", multiply(a, b))
        print("Division:", divide(a, b))
        print("Square Root of first number:", square_root(a))
        print("Exponentiation:", exponentiate(a, b))
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()