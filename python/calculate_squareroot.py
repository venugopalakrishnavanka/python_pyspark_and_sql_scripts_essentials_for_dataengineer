import math

def check_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(math.isqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    val = int(input("Enter integer: \n"))
    if check_prime(val):
        print(f"{val} is PRIME. Square root: {math.sqrt(val):.4f}")
    else:
        print(f"{val} is NOT a prime number.")