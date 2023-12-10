import os


def extract_calibration_value(line):
    """Extracts the calibration value from a line by combining the first and last digits."""
    # Finding the first digit
    first_digit = next((char for char in line if char.isdigit()), None)
    # Finding the last digit
    last_digit = next((char for char in reversed(line) if char.isdigit()), None)

    # If either first or last digit is not found, return 0
    if first_digit is None or last_digit is None:
        return 0

    # Combine first and last digits and convert to integer
    return int(first_digit + last_digit)


def calculate_total_calibration_value_from_file(filename):
    """Calculates the total calibration value from a file."""
    total_sum = 0
    with open(filename, "r") as file:
        # Iterate over each line in the file
        for line in file:
            # Extract the calibration value from the line and add it to the total sum
            total_sum += extract_calibration_value(line.strip())

    return total_sum


# Get the directory of the current script
script_dir = os.path.dirname(__file__)
# Construct the full path to the input file
input_file = os.path.join(script_dir, "input")

# Calculate the total calibration value from the file
total = calculate_total_calibration_value_from_file(input_file)
print(
    f"Total sum of calibration values from file: {total}"
)  # Print sum and copy into browser to check solution
