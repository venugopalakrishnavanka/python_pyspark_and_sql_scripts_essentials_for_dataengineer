def find_largest(a: float, b: float, c: float) -> float:
    return max(a, b, c)

if __name__ == "__main__":
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    n3 = float(input("Enter third number: "))
    
    print(f"The largest number is: {find_largest(n1, n2, n3)}")