from collections import Counter

log_path = input("Enter the path to the log file: ")

with open(log_path, 'r') as log_file:
    lines = log_file.readlines()

print(f"Successfully loaded {len(lines)} lines from the log file.")

error_count = 0
warning_count = 0

errors = []
warnings = []
error_messages = []
warning_messages = []

for line in lines:
    if "ERROR" in line:
        error_count += 1
        errors.append(line.strip())

        error_message = line.split("ERROR:")[1].strip()
        error_messages.append(error_message)

        error_frequency = Counter(error_messages)
    elif "WARNING" in line:
        warning_count += 1
        warnings.append(line.strip())

        warning_message = line.split("WARNING:")[1].strip()
        warning_messages.append(warning_message)

        warning_frequency = Counter(warning_messages)

print(f"Errors found: {error_count}")
print(f"Warnings found: {warning_count}")

print("\nList of Errors:")
for error in errors:
    print(error)

print("\nList of Warnings:")
for warning in warnings:
    print(warning)

print("\nError Frequency:")
for message, count in error_frequency.items():
    if count > 1:
        print(f"{message} - occurred {count} times")

print("\nWarning Frequency:")
for message, count in warning_frequency.items():
    if count > 1:
        print(f"{message} - occurred {count} times")