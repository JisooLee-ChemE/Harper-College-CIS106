total_bonus = 0

file = open("M7P3.txt", "r")

last_name = file.readline().strip()

while last_name != "":
    salary = float(file.readline())

    if salary >= 100000:
        bonus_rate = 0.20
    elif salary >= 50000:
        bonus_rate = 0.15
    else:
        bonus_rate = 0.10

    bonus = salary * bonus_rate
    total_bonus = total_bonus + bonus

    print("Last Name:", last_name)
    print("Salary: $", format(salary, ",.2f"))
    print("Bonus: $", format(bonus, ",.2f"))
    print()

    last_name = file.readline().strip()

file.close()

print("Total bonuses paid: $", format(total_bonus, ",.2f"))