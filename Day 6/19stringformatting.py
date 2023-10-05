# Format a phone number or date string in a specific way.
phone_number = input("Enter a phone number (digits only): ")
if phone_number.isdigit() and len(phone_number) == 10:
    formatted_phone_number = f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}"
    print("Formatted phone number:", formatted_phone_number)
else:
    print("Invalid input. Please enter a 10-digit number.")

