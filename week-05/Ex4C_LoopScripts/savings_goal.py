bank_balance = 50
savings_goal = 2500
weekly_savings = 200

while bank_balance < savings_goal:
    bank_balance = bank_balance + weekly_savings
    print("This week my balace increased to", bank_balance)
    if bank_balance > savings_goal / 2:
        print("Almost there! This week my balance is up to", bank_balance)
    if bank_balance >= savings_goal * 0.75:
        bank_balance = bank_balance - 50
        print("So close! After treating myself, my balance is up to", bank_balance)
print("Goal met! My current balance is", bank_balance)

