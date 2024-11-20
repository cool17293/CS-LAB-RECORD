# Taking user input for the number
number = int(input("Enter a number: "))

# Finding the last digit
last_digit = number % 10

# Checking if the last digit is divisible by 3
if last_digit % 3 == 0:
    print("The last digit of the number is divisible by 3.")
else:
    print("The last digit of the number is not divisible by 3.")