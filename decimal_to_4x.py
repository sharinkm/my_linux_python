#  takes a single-digit decimal number X, 
# and returns the value of: X + XX + XXX + XXXX

class RepeatedDigitSum:
    def __init__(self, digit):
        """
        Initializes the class with a digit. Validates input.
        """
        if not isinstance(digit, int):
            raise TypeError("Input must be an integer.")
        if digit < 0 or digit > 9:
            raise ValueError("Input must be a single decimal digit between 0 and 9.")
        self.digit = digit

    def calculate(self):
        """
        Calculates X + XX + XXX + XXXX based on the digit.
        """
        str_digit = str(self.digit)
        total = 0
        for i in range(1, 5):
            repeated_number = int(str_digit * i)
            total += repeated_number
        return total


if __name__ == "__main__":
    try:
        user_input = input("Enter a single decimal digit (0–9): ").strip()

        # Try converting input to integer
        if not user_input.isdigit():
            raise ValueError("Input must be a numeric digit.")
        
        digit = int(user_input)
        calculator = RepeatedDigitSum(digit)
        result = calculator.calculate()
        print(f"Result for digit {digit}: {result}")

    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
