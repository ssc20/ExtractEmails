README for Email Filtering Scripts

---

Overview

This project provides two Python scripts for processing CSV files containing email addresses:

1. Valid Email Extractor: Isolates and exports valid email addresses.
2. Invalid Email Extractor: Isolates and exports invalid email addresses.

These scripts use regular expressions to validate email addresses and identify disallowed characters.

---

Files Included

- `valid_email_filter.py`: Script to extract valid email addresses from a CSV.
- `invalid_email_filter.py`: Script to extract invalid email addresses from a CSV.

---

Features

1. Valid Email Extractor:
   - Extracts email addresses that follow a valid format.
   - Filters out entries with disallowed characters like `()`, `{}`, `[]`, etc.
   - Outputs valid email addresses into a new CSV file.

2. Invalid Email Extractor:
   - Identifies entries that do not conform to standard email address formats.
   - Captures invalid email addresses or entries with disallowed characters.
   - Outputs invalid email entries into a separate CSV file.

---

Requirements

- Python 3.7 or later
- CSV file with email addresses in one or multiple columns

---

Installation

1. Clone or download the repository.
2. Ensure Python is installed on your system.
3. Install any necessary dependencies (if required by your environment):
   ```bash
   pip install -r requirements.txt
   ```
   (Note: This project does not require additional libraries beyond Python's standard library.)

---

Usage

Valid Email Extractor

1. Open the `valid_email_filter.py` file and update the following variables:
   ```python
   input_file = 'input.csv'  # Path to your input CSV
   output_file = 'valid_emails.csv'  # Path for the output CSV
   ```

2. Run the script:
   ```bash
   python valid_email_filter.py
   ```

3. The valid email addresses will be written to `valid_emails.csv`.

Invalid Email Extractor

1. Open the `invalid_email_filter.py` file and update the following variables:
   ```python
   input_file = 'input.csv'  # Path to your input CSV
   output_file = 'invalid_emails.csv'  # Path for the output CSV
   ```

2. Run the script:
   ```bash
   python invalid_email_filter.py
   ```

3. The invalid email addresses will be written to `invalid_emails.csv`.

---

Customization

Both scripts are designed to work with all columns in the input CSV file. If you need to target specific columns or add custom logic, you can modify the script by updating the relevant loops or conditions.

---

Notes

- Ensure that your input CSV file is properly formatted.
- The output files will overwrite existing files with the same names. Be cautious if you have important data in the output file path.
- These scripts are intended for basic email validation and may not catch all edge cases.

---

License

This project is open-source and available under the MIT License.
