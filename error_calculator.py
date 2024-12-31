# calculator.py
def safe_input(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        raise ValueError("Invalid input. Please enter a number.")

def validate_division(b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return b

def validate_square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return a
