# Research and Learning

This document records the research, learning and problem-solving that took place while developing the Game Log Analyser.

# Initial Approach

I decided to create a game log analysis tool using Python. I chose Python because it is commonly used for scripting and automation, making it relevant to DevOps while also allowing me to improve my existing Python knowledge.

The initial goal was to create a small command-line application that could take a game log file as input, identify errors and warnings, and present useful information about problems found within the log.

I deliberately started with basic functionality and expanded the program incrementally rather than attempting to build the entire application at once.

# Using Counter for Frequency Analysis

I wanted the analyser to do more than simply count the total number of errors and warnings. Repeated messages can indicate recurring problems, so I wanted to identify how frequently individual messages appeared.

I learned about Python's `Counter` class from the `collections` module, which provides a simple way of counting repeated values.

The analyser extracts the message following `ERROR:` or `WARNING:` and uses `Counter` to calculate how often each message occurs.

During development I also discovered an edge case where an entry containing only `ERROR:` or `WARNING:` resulted in an empty string being added to the frequency data. I changed the logic so the entry is still counted as an error or warning, but an empty message is not added to the frequency analysis.

# Refactoring into Functions

The first version of the program was written as a sequence of instructions. As the analyser gained more functionality, I refactored the code into separate functions for validation, reading the file, analysing the contents, displaying the results and saving the report.

This helped me understand how separating responsibilities makes code easier to read, test and maintain. It also made it possible to test the analysis functionality independently from the rest of the application.

# Error Handling and Input Validation

I added input validation so that the analyser only accepts `.log` files. I also used `try` and `except` to handle `FileNotFoundError` and `PermissionError`, allowing the program to provide a useful error message instead of displaying a Python traceback.

During testing, I deliberately provided a path to a file that did not exist. The original implementation produced a traceback, which led me to add the exception handling and test the same scenario again.

I also made the file extension check case-insensitive by converting the path to lowercase before checking the extension.

# Unit Testing

I researched Python's built-in `unittest` framework and used it to create automated tests for the core `analyse_log()` function.

The tests cover logs containing errors and warnings, logs containing no problems, repeated messages and entries where `ERROR:` or `WARNING:` has no message.

Writing the tests exposed an issue where empty error and warning messages were being included in the frequency analysis. I corrected the analysis logic and reran the tests to verify the fix.

I also learned about Python's `if __name__ == "__main__":` pattern. Initially, importing `analyse_log()` into the test file caused the entire application to run and ask for a log file path. Moving the application's execution into a `main()` function and using the `__main__` check allowed the functions to be imported for testing without starting the application.

After these changes, all three automated tests passed successfully.

# Research Approach

When I encountered concepts or behaviour I was unsure about, I researched them as they became relevant rather than trying to learn everything before starting development.

Areas I researched included:

- Python's `Counter` class and how it can be used to identify repeated values.
- Exception handling using `try` and `except`.
- File handling and the different modes available when opening files.
- Python's `unittest` framework and how assertions are used to verify expected behaviour.
- The purpose of `if __name__ == "__main__":` when creating code that can also be imported by another Python file.

I tested the concepts within the project rather than assuming they worked as expected. This included deliberately providing invalid file paths, using logs with empty error and warning messages, using logs with no errors or warnings, and creating repeated messages to verify the frequency analysis.

# Lessons Learned

The project reinforced the importance of building software incrementally and testing changes as they are introduced. Starting with a simple log reader made it easier to add analysis, reporting, validation and automated testing without making the program unnecessarily complex.

I also gained a better understanding of separating functionality into functions, handling expected failures cleanly and writing automated tests for specific behaviour.

One of the most useful lessons was that testing can reveal issues that are easy to overlook during normal use. The empty-message issue and the application running when imported by the test file both resulted in changes that improved the overall structure and reliability of the program.