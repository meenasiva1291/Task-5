from functools import reduce

fibonacci = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])[:n]

# Example usage:
n=int(input("Enter a number:"))
print(f"fibonacci series of the given number is: ", fibonacci(n))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
