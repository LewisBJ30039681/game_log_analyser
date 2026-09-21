# AI Usage

# Tools Used

I used ChatGPT during the development of this project.

# How AI Was Used

ChatGPT was primarily used as a learning and development assistant. I used it to:

- Discuss and refine the initial project idea.
- Break the project into smaller development steps.
- Explain Python concepts that I was unfamiliar with or needed a refresher on.
- Discuss approaches to structuring and refactoring the program.
- Learn about `Counter`, `unittest` and the `if __name__ == "__main__":` pattern.
- Review code I had written and identify potential issues.
- Suggest edge cases that could be tested.
- Help structure the project documentation.

I generally implemented changes incrementally and ran the program after each change to confirm that I understood the behaviour and that it worked as expected.

# Verification of AI Suggestions

I did not assume that AI-generated suggestions were correct. Changes were implemented and tested locally before being kept in the project.

For example, I tested invalid file paths to verify exception handling, created different sample log entries to verify error and warning detection, and used automated unit tests to check the output of the analysis function.

The unit tests also exposed an issue with empty error and warning messages being included in the frequency analysis. The code was changed and the tests were rerun until all three tests passed.

# Incorrect or Unhelpful Suggestions

Not every AI suggestion was followed directly. I reviewed suggestions against the current state of my code and tested changes before accepting them.

For example, after I renamed the analysis function from `analyze_log()` to the British spelling `analyse_log()`, ChatGPT initially suggested that the test file was using the wrong function name. I recognised that the function had already been renamed and clarified this rather than changing the working code.

There were also cases where suggested code duplicated functionality that was already present. These were identified during review and simplified so that each function had a clear responsibility.

Using AI in this way reinforced the importance of understanding the existing code and treating AI output as a suggestion to evaluate rather than something to copy without verification.