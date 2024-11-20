#perfect number

number = int(input("Enter a number: "))

sum_of_divisors = 0

for i in range(1, number):
    if number % i == 0:
        sum_of_divisors += i

if sum_of_divisors == number:
    print(number, "is a Perfect number.")
else:
    print(number, "is not a Perfect number.")