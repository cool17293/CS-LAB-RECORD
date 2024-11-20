

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "undefined (division by zero)"
modulus = num1 % num2 if num2 != 0 else "undefined (modulus by zero)"
exponentiation = num1  num2
floor_division = num1 // num2 if num2 != 0 else "undefined (floor division by zero)"


print(f"\nResults of arithmetic operations:")
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} % {num2} = {modulus}")
print(f"{num1}  {num2} = {exponentiation}")
print(f"{num1} // {num2} = {floor_division}")