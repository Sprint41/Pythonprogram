# Concatenate strings and numbers into a single string for display.
import datetime
original_date_string = input("Enter a date (YYYY-MM-DD): ")

try:
    original_date = datetime.datetime.strptime(original_date_string, "%Y-%m-%d")
    formatted_date = original_date.strftime("%m/%d/%Y")
    print("Formatted date:", formatted_date)
except ValueError:
    print("Invalid date format. Please enter a date in YYYY-MM-DD format.")
