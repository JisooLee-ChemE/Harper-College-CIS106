def compute_scores(exam1, exam2, exam3):
    total_points = exam1 + exam2 + exam3
    average_score = total_points / 3

    return total_points, average_score

last_name = input("Enter the student's last name: ")
exam1 = float(input("Enter the score for Exam 1: "))
exam2 = float(input("Enter the score for Exam 2: "))
exam3 = float(input("Enter the score for Exam 3: "))

total_points, average_score = compute_scores(exam1, exam2, exam3)

print("Last Name:", last_name)
print("Total Points: ", format(total_points, ".2f"))
print("Average Score: ", format(average_score, ".2f"))