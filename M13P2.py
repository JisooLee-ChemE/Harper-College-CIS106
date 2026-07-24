def display_students(last_names, exam_scores):
    print("Students and their exam scores:")
    for i in range(len(last_names)):
        print("Last Name:", last_names[i])
        print("Exam Score:", exam_scores[i])
        print()


def display_students_reverse(last_names, exam_scores):
    print("Students and their exam scores in reverse order:")
    for i in range(len(last_names) - 1, -1, -1):
        print("Last Name:", last_names[i])
        print("Exam Score:", exam_scores[i])
        print()

last_name = ["Maxwell", "Johnson", "Williams", "Jones", "Brown", "Lee", "Smith", "Davis", "Miller", "Wilson"]

exam_scores = [85, 92, 38, 50, 48, 95, 80, 67, 91, 89]

display_students(last_name, exam_scores)
display_students_reverse(last_name, exam_scores)