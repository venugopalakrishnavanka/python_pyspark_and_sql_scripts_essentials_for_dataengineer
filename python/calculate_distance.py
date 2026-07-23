import math

def calculate_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

if __name__ == "__main__":
    x1, y1 = float(input("x1: ")), float(input("y1: "))
    x2, y2 = float(input("x2: ")), float(input("y2: "))
    print(f"Distance: {calculate_distance(x1, y1, x2, y2):.4f}")