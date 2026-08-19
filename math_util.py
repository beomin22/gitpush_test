def average(numbers):
    if not numbers:
        raise ValueError("numbers must be a non-empty list")
    return sum(numbers) / len(numbers)
