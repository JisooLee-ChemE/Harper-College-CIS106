last_name = input("Enter your last name: ")
midterm_score = float(input("Enter the midterm score: "))
final_score = float(input("Enter the final score: "))

total_score = midterm_score * 0.40 + final_score * 0.60

print(f"Student Last Name: {last_name}")
print(f"The total score is: {total_score:.2f}")