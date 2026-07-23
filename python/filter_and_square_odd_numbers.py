def odd_squares():
    num_elems = int(input("Enter the number of elements: \n"))
    input_list = [int(input(f"Enter element {i + 1}: \n")) for i in range(num_elems)]
    
    print("Input elements list:", input_list)

    # Filter odd numbers and square them
    result = [elem ** 2 for elem in input_list if elem % 2 != 0]
    print("Resulting squared list (odd numbers only):", result)

if __name__ == "__main__":
    odd_squares()