from collections import Counter

def main():
    # Main function to run the log analysis
    log_path = input("Enter the path to the log file: ")
    validate_log_file(log_path)
    lines = read_log_file(log_path)
    print(f"Successfully loaded {len(lines)} lines from the log file.")
    error_count, warning_count, errors, warnings, error_frequency, warning_frequency = analyse_log(lines)
    display_results(error_count, warning_count, errors, warnings, error_frequency, warning_frequency)
    save_report(error_count, warning_count, errors, warnings, error_frequency, warning_frequency)

def read_log_file(log_path):
    # Read the log file and return its lines, handling potential errors
    try:
        with open(log_path, 'r') as log_file:
            lines = log_file.readlines()
    except FileNotFoundError:
        print(f"Error: The file at '{log_path}' was not found.")
        exit(1)
    except PermissionError:
        print(f"Error: Permission denied when trying to read the file at '{log_path}'.")
        exit(1)
    return lines

def analyse_log(lines):
    # Analyse the log lines to count errors and warnings, and track their frequency
    error_count = 0
    warning_count = 0

    errors = []
    warnings = []
    error_messages = []
    warning_messages = []

    for line in lines:
        if "ERROR:" in line:
            error_count += 1
            errors.append(line.strip())

            error_message = line.split("ERROR:", 1)[1].strip()
            if error_message:
                error_messages.append(error_message)
            
        elif "WARNING:" in line:
            warning_count += 1
            warnings.append(line.strip())

            warning_message = line.split("WARNING:", 1)[1].strip()
            if warning_message:
                warning_messages.append(warning_message)

    error_frequency = Counter(error_messages)
    warning_frequency = Counter(warning_messages)

    return error_count, warning_count, errors, warnings, error_frequency, warning_frequency

def display_results(error_count, warning_count, errors, warnings, error_frequency, warning_frequency):
    # Display the analysis results in a readable format
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

def save_report(error_count, warning_count, errors, warnings, error_frequency, warning_frequency):
    # Save the analysis report to a text file
    with open("analysis_report.txt", "w") as report_file:
        report_file.write("Game Log Analysis Report\n")
        report_file.write("========================\n\n")
        report_file.write(f"Errors found: {error_count}\n")
        report_file.write(f"Warnings found: {warning_count}\n\n")

        report_file.write("List of Errors:\n")
        for error in errors:
            report_file.write(f"{error}\n")

        report_file.write("\nList of Warnings:\n")
        for warning in warnings:
            report_file.write(f"{warning}\n")

        report_file.write("\nRepeated Errors:\n")
        if any(count > 1 for count in error_frequency.values()):
            for message, count in error_frequency.items():
                if count > 1:
                    report_file.write(f"{message} - occurred {count} times\n")
        else:
            report_file.write("No repeated errors found.\n")

        report_file.write("\nRepeated Warnings:\n")
        if any(count > 1 for count in warning_frequency.values()):
            for message, count in warning_frequency.items():
                if count > 1:
                    report_file.write(f"{message} - occurred {count} times\n")
        else:
            report_file.write("No repeated warnings found.\n")

def validate_log_file(log_path):
    # Validate that the log file has a .log extension
    if not log_path.lower().endswith('.log'):
        print("Error: The log file must have a .log extension.")
        exit(1)

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
