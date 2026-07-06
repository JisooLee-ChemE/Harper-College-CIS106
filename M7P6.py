student_count = 0

response = input("Do you want to enter student information? Enter Yes to continue: ")

while response == "Yes" or response == "yes" or response == "Y" or response == "y":
    last_name = input("Enter the student's last name: ")
    exam1 = float(input("Enter the student's first exam score: "))
    exam2 = float(input("Enter the student's second exam score: "))

    average_score = (exam1 + exam2) / 2

    print("Last Name:", last_name)
    print("Average Exam Score:", format(average_score, ".2f"))
    print()

    student_count = student_count + 1

    response = input("Do you want to enter student information? Enter Yes to continue: ")

print("Number of Students:", student_count)