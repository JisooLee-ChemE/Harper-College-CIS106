ticket_symbol = input("Enter the ticket symbol: ")
shares = float(input("Enter the number of shares: "))
cost_per_share = float(input("Enter the cost per share: "))

amount_invested = shares * cost_per_share

print(f"Stock Symbol: {ticket_symbol}")
print(f"Amount Invested: ${amount_invested:.2f}")