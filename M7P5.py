total_tuition = 0
student_count = 0

file = open("M7P5.txt", "r")

last_name = file.readline().strip()

while last_name != "":
    district_code = file.readline().strip()
    credits_taken = int(file.readline())

    if district_code == "l":
        cost_per_credit = 250
    else:
        cost_per_credit = 500

    tuition_owed = credits_taken * cost_per_credit
    total_tuition = total_tuition + tuition_owed
    student_count = student_count + 1

    print("Last Name:", last_name)
    print("Credits Taken:", credits_taken)
    print("Tuition Owed: $", format(tuition_owed, ",.2f"))
    print()

    last_name = file.readline().strip()

file.close()

print("Total Tuition Owed: $", format(total_tuition, ",.2f"))
print("Number of Students:", student_count)