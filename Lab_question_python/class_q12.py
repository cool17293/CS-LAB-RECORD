#Armstrong number
number = int(input("Enter a number: "))

num_of_digits = len(str(number))

sum_of_powers = 0

temp = number

while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** num_of_digits
    temp //= 10

if sum_of_powers == number:
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")