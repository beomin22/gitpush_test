def find_max(numbers):
    if not numbers:
        raise ValueError("numbers must be a non-empty list")
    return max(numbers)
