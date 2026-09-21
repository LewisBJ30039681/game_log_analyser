# game_log_analyser
A python tool for analysing game log files and summarising errors and warnings.

# Why I built this
I created this project to explore how log analysis can be used to quickly identify recurring problems within software. I chose game logs because of my background and intrests in game development, while the underlying concepts are applicable to areas like software monitoring and DevOps.

# Features
- Reads `.log` files provided by the user
- Validates the file type before processing
- Handles missing files and permission errors
- Detects and counts errors and warnings
- Lists individual error and warning entries
- Identifies repeated error and warning messages
- Generates a text report containing the analysis
- Includes automated unit tests for the core analysis functionality

# How to run
- Python 3 (no external python packages are required)
- Clone the repo and navigate to the project directory
- Run:
```bash
python analyser.py

when promted use sample_logs/sample.log
results will be displayed in the terminal and saved to analysis_report.txt

# Testing

The project uses Python's built-in `unittest` framework to test the core log analysis functionality.

The tests currently cover:

- Correct detection of errors and warnings
- Logs containing no errors or warnings
- Detection and counting of repeated errors and warnings
- Handling of error and warning entries with empty messages

Run the tests with:

```bash
python -m unittest test_analyser.py

## Project Structure

```text
game_log_analyser/
├── sample_logs/
│   └── sample.log
├── analyser.py
├── test_analyser.py
├── README.md
├── RESEARCH.md
└── AI.md