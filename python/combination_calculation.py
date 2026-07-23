import math

def n_cr(n: int, r: int) -> float:
    if r > n or n < 0 or r < 0:
        raise ValueError("Invalid parameters for nCr calculation.")
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))

if __name__ == "__main__":
    n_val = int(input("Enter n: "))
    r_val = int(input("Enter r: "))
    print(f"nCr ({n_val}C{r_val}) = {int(n_cr(n_val, r_val))}")