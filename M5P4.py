principle = float(input("Enter the principal amount: "))
years = int(input("Enter the number of years: "))

if principle > 100000 and years == 5:
    interest_rate = 0.06
elif principle <= 100000 and principle >= 50000 and years == 10:
    interest_rate = 0.05
elif principle <= 100000 and principle >= 50000 and years == 5:
    interest_rate = 0.04
else:
    interest_rate = 0.02

first_year_interest = principle * interest_rate

print(f"Principal Amount: ${principle:.2f}")
print(f"Interest Rate: {interest_rate * 100:.2f}%")
print(f"First Year Interest: ${first_year_interest:.2f}")