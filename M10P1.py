def compute_forecast(month, sales):
    if month == "Jan" or month == "Feb" or month == "Mar":
        forecast_percent = 0.10
    elif month == "Apr" or month == "May" or month == "Jun":
        forecast_percent = 0.15
    elif month == "Jul" or month == "Aug" or month == "Sep":
        forecast_percent = 0.20
    else:
        forecast_percent = 0.25

    next_month_sales = sales * (1 + forecast_percent)

    return next_month_sales

response = input("Do you want to enter sales information? Enter Yes to continue: ")

while response == "Yes" or response == "yes" or response == "Y" or response == "y":
    last_name = input("Enter last name: ")
    month = input("Enter month (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): ")
    sales = float(input("Enter sales: "))

    next_month_sales = compute_forecast(month, sales)

    print ("Last Name:", last_name)
    print ("Month:", month)
    print ("Sales: $", format(sales, ".2f"))
    print ("Next Month Sales Forecast: $", format(next_month_sales, ".2f"))
    print()

    response = input("Do you want to enter sales information? Enter Yes to continue: ")