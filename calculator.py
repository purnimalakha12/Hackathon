def water_usage_meter_calculator_daily():
    print("Water Usage Calculator Based on Daily Inputs\n")

    # Input: Daily water usage for each day of the week
    daily_usages = []
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days:
        usage = float(input(f"Enter the water usage for {day} (in gallons): "))
        daily_usages.append(usage)

    # Calculate total weekly usage and average daily usage
    total_weekly_usage = sum(daily_usages)
    average_daily_usage = total_weekly_usage / 7

    # Output: Display daily usage, total weekly usage, and daily average usage
    print("\nDaily Water Usage:")
    for i, usage in enumerate(daily_usages):
        print(f"{days[i]}: {usage:.2f} gallons")

    print("\nTotal Water Usage for the Week: {:.2f} gallons".format(total_weekly_usage))
    print("Average Daily Water Usage: {:.2f} gallons".format(average_daily_usage))

    # Optional: Provide feedback based on daily average
    if average_daily_usage > 300:
        print("\nYour water usage is higher than average. Consider checking for leaks or adopting water-saving habits.")
    elif average_daily_usage < 150:
        print("\nGreat job! Your water usage is below average. Keep up the good work conserving water!")
    else:
        print("\nYour water usage is within a typical range. Consider some additional water-saving measures if you’d like to reduce it further.")

# Run the calculator
water_usage_meter_calculator_daily()