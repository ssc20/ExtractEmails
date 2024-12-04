import csv
import re

# Define a function to validate email addresses
def is_valid_email(email):
    # Regex to match typical email patterns
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # Check for disallowed characters in the email address
    disallowed_chars = set("(){}[];:'\"<>,")
    if any(char in email for char in disallowed_chars):
        return False
    return re.match(email_regex, email) is not None

def isolate_invalid_emails(input_csv, output_csv):
    invalid_emails = []

    # Read the input CSV
    with open(input_csv, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for cell in row:
                cell = cell.strip()
                if not is_valid_email(cell):  # Extract invalid emails
                    invalid_emails.append(cell)

    # Write invalid emails to output CSV
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for email in invalid_emails:
            writer.writerow([email])

# Input and output file paths
input_file = 'Book2.csv'  # Replace with your input CSV file path
output_file = 'invalid_emails.csv'  # Replace with your desired output CSV file path

# Run the email isolation process
isolate_invalid_emails(input_file, output_file)

print(f"Invalid email addresses have been written to {output_file}")