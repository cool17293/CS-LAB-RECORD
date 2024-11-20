
n1 = int(input("Enter the first number (n1): "))
n2 = int(input("Enter the second number (n2): "))

print(f"Prime numbers between {n1} and {n2}:")

for num in range(n1, n2 + 1):
    if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
        print(num)