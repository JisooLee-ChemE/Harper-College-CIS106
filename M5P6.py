last_name = input("Enter your last name: ")
salary = float(input("Enter your salary: "))
job_level = int(input("Enter your job level: "))

if job_level >= 10:
    bonus_rate = 0.25
elif job_level >= 5 and job_level <= 9:
    bonus_rate = 0.20
else:
    bonus_rate = 0.10

bonus_amount = salary * bonus_rate

print(f"Last Name: {last_name}")
print(f"Bounus Amount: ${bonus_amount:.2f}")