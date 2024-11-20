students = []

for _ in range(5):
    name = input("Enter student's name: ")
    roll_number = int(input("Enter roll number: "))
    age = int(input("Enter age: "))
    
    students.append([name, roll_number, age])


students.sort(key=lambda student: student[1])

print("\nSorted list of students based on roll number:")
for student in students:
    print(f"Name: {student[0]}, Roll Number: {student[1]}, Age: {student[2]}")