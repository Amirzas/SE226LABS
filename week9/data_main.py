from data_package import remove_duplicates, strip_whitespaces, calculate_mean, find_maximum, find_minimum

raw_input = input("Enter a comma-separated list of numbers (e.g., 12, 5, 12, 8 , 21): ")

tokens = raw_input.split(",")
stripped = strip_whitespaces(tokens)

valid = True
numbers = []

for item in stripped:
    if item.lstrip("-").replace(".", "").isdigit():
        numbers.append(float(item))
    else:
        valid = False
        break

if not valid:
    print("Data Error: Please make sure you only enter numbers separated by commas.")
else:
    cleaned = remove_duplicates(numbers)
    print(f"Cleaned and unique data: {cleaned}")
    print("-" * 20)
    print(f"Mean: {calculate_mean(cleaned):.2f}")
    print(f"Maximum: {find_maximum(cleaned)}")
    print(f"Minimum: {find_minimum(cleaned)}")