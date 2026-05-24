# Step 1: Get user input
phone_number = input("Enter a U.S. phone number: ")
# Step 2: Remove leading/trailing spaces
phone_number = phone_number.strip()
# Step 3: Replace common separators with spaces
separators = ['-', '(', ')', '.']
for sep in separators:
    phone_number = phone_number.replace(sep, ' ')
# Step 4: Split into chunks and join digits
digits = phone_number.split()
cleaned_number = ''.join(digits)
# Step 5: Check if the cleaned number has exactly 10 digits
if len(cleaned_number) == 10 and cleaned_number.isdigit():
    # Step 6: Format the number
    formatted_number = f"({cleaned_number[:3]}) {cleaned_number[3:6]}-{cleaned_number[6:]}"
    print(f"Formatted Phone Number: {formatted_number}")
else:
    # Step 7: Print error message
    print("Please enter exactly 10 digits.")
