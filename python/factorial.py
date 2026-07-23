# Iterative approach
def factorial_iterative(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Recursive approach
def factorial_recursive(n: int) -> int:
    if n in (0, 1):
        return 1
    return n * factorial_recursive(n - 1)

if __name__ == "__main__":
    num = int(input("Enter a positive integer: "))
    print(f"Iterative Factorial: {factorial_iterative(num)}")
    print(f"Recursive Factorial: {factorial_recursive(num)}")