
choice = input("Enter 1 for Fahrenheit to Celsius or 2 for Celsius to Fahrenheit: ")
temp = float(input("Enter the temperature: "))

if choice == '1':
    result = (temp - 32) * 5 / 9
    print(f"{temp} Fahrenheit is {result:.2f} Celsius")
elif choice == '2':
    result = (temp * 9 / 5) + 32
    print(f"{temp} Celsius is {result:.2f} Fahrenheit")
else:
    print("Invalid choice.")