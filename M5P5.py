tickets = int(input("Enter the number of tickets: "))

if tickets >= 25:
    price_per_ticket = 50
elif tickets >= 10 and tickets <=24:
    price_per_ticket = 60
elif tickets >= 5 and tickets <=9:
    price_per_ticket = 70
else:
    price_per_ticket = 75

total_cost = tickets * price_per_ticket

print(f"Number of Tickets: {tickets}")
print(f"Price per Ticket: ${price_per_ticket:.2f}")
print(f"Total Cost: ${total_cost:.2f}")