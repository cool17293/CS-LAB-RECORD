
n1 = int(input("Enter the first number (n1): "))
n2 = int(input("Enter the second number (n2): "))


print(f"Odd numbers between {n1} and {n2}:")

for num in range(n1, n2 + 1):
    if num % 2 != 0:  # Check if the number is odd
        print(num)