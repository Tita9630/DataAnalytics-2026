current_saving = 2500
interest_rate = 8
years = 72 / interest_rate
doubled_balance = current_saving * 2

print(f"Your current savings is {format(current_saving, '.2f')}.")
print(f"At a {interest_rate}% interest rate, your savings account will be worth {format(doubled_balance, '.2f')} in {format(years, '.1f')} years.")