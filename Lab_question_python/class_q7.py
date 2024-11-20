# Taking user input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Finding the lowest number
if num1 < num2:
    print("The lowest number is:", num1)
elif num2 < num1:
    print("The lowest number is:", num2)
else:
    print("Both numbers are equal.")