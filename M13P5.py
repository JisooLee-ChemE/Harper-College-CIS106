def create_student_averages(students):
    student_averages = {}
    
    for name, grades in students.items():
        total = grades[0] + grades[1] + grades[2]
        average = total / 3
        student_averages[name] = average

    return student_averages

students = {
    "Maxwell": [85, 88, 90],
    "Johnson": [92, 94, 96],
    "Williams": [38, 40, 42],
    "Jones": [50, 52, 54],
    "Lee": [95, 97, 99],
    "Smith": [80, 82, 84],
    "Davis": [67, 69, 71],
    "Parker": [91, 93, 95],
    "Muller": [89, 91, 93],
    "Brown": [48, 50, 52]
}

student_averages = create_student_averages(students)

exam1_total = 0
exam2_total = 0
exam3_total = 0
student_count = 0

print(f"{'Student Name':<15}{'Grade 1':>10}{'Grade 2':>10}{'Grade 3':>10}{'Average':>10}")
print("-" * 55)

for name, grades in students.items():
    average = student_averages[name]

    print(f"{name:<15}{grades[0]:>10.2f}{grades[1]:>10.2f}{grades[2]:>10.2f}{average:>10.2f}")

    exam1_total = exam1_total + grades[0]
    exam2_total = exam2_total + grades[1]
    exam3_total = exam3_total + grades[2]
    student_count = student_count + 1

exam1_average = exam1_total / student_count
exam2_average = exam2_total / student_count
exam3_average = exam3_total / student_count

print("-" * 55)
print(f"{'Exam Average:':<15}{exam1_average:>10.2f}{exam2_average:>10.2f}{exam3_average:>10.2f}")