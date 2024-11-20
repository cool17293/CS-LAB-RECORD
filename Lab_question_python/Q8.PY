
shyam_age = int(input("Enter Shyam's age: "))
dugu_age = int(input("Enter Dugu's age: "))
ishan_age = int(input("Enter Ishan's age: "))


if shyam_age < dugu_age and shyam_age < ishan_age:
    youngest = "Shyam"
elif dugu_age < shyam_age and dugu_age < ishan_age:
    youngest = "Dugu"
else:
    youngest = "Ishan"


print(f"The youngest is {youngest}.")