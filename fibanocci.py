
# Program that calculates the sum of the first 100 even-valued Fibonacci numbers 



class EvenFibonacciSum:
    def __init__(self, count):
        """
        Initialize the class with the number of even Fibonacci numbers to sum.
        """
        self.count = count

    def calculate(self):
        """
        Calculates the sum of the first `self.count` even Fibonacci numbers
        using an optimized recurrence relation.
        """
        even_fibs = []
        a, b = 2, 8  # First two even Fibonacci numbers
        even_fibs.append(a)
        even_fibs.append(b)

        while len(even_fibs) < self.count:
            c = 4 * b + a  # Efficient recurrence for even Fibs
            even_fibs.append(c)
            a, b = b, c

        return sum(even_fibs)

    def run(self):
        """
        Executes the calculation and prints the result.
        """
        result = self.calculate()
        print(f"Sum of first {self.count} even Fibonacci numbers: {result}")


if __name__ == "__main__":
    calculator = EvenFibonacciSum(count=100)
    calculator.run()
