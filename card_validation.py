# Function to validate a credit card number using Luhn's algorithm
def validate_card(card_number):
    # Reversing the card number and converting to a list
    digits = [int(digit) for digit in str(card_number)[::-1]]

    # Double every second digit starting from the second digit
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        # If the doubled digit is greater than 9, subtract 9 from it
        if digits[i] > 9:
            digits[i] -= 9

    # Sum all the digits
    total_sum = sum(digits)

    # If the sum is divisible by 10, the card is valid
    return total_sum % 10 == 0

# Prompt the user to enter the credit card number
card_number = input("Enter the credit card number: ")

# Validate the card and print the result
if validate_card(card_number):
    print("The credit card number is valid.")
else
    print("The credit card number is invalid.")
