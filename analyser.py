log_path = input("Enter the path to the log file: ")

with open(log_path, 'r') as log_file:
    lines = log_file.readlines()

print(f"Successfully loaded {len(lines)} lines from the log file.")

error_count = 0
warning_count = 0

for line in lines:
    if "ERROR" in line:
        error_count += 1
    elif "WARNING" in line:
        warning_count += 1

print(f"Errors found: {error_count}")
print(f"Warnings found: {warning_count}")