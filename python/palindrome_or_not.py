def is_palindrome(text: str) -> bool:
    cleaned_str = text.strip().lower()
    reversed_str = cleaned_str[::-1]
    return cleaned_str == reversed_str

if __name__ == "__main__":
    s = input("Enter string to check: \n")
    if is_palindrome(s):
        print(f"'{s}' is a palindrome!")
    else:
        print(f"'{s}' is NOT a palindrome.")