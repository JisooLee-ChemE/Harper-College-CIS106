students = {
    "Maxwell": 85,
    "Johnson": 92,
    "Williams": 38,
    "Jones": 50,
    "Lee": 95,
    "Smith": 80,
    "Davis": 67,
    "Parker": 91,
    "Muller": 89,
    "Brown": 48
}

total_grade = 0
student_count = 0

print(f"{'Student Name':<20}{'Grade':<10}")
print("-" * 30)

for name, grade in students.items():
    print(f"{name:<20}{grade:<10.2f}")
    total_grade = total_grade + grade
    student_count = student_count + 1

class_average = total_grade / student_count

print("-" * 30)
print(f"{'Class Average:':<20}{class_average:<10.2f}")