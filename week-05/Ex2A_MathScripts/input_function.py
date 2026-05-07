total_asset = int(input("What is your asset?"))
total_debt = int(input("What is your debt?"))
print(f"Your net_worth is {total_asset - total_debt}")
# pitfall- Before specifying the type, I used words to response not numeric values and
# got error message saying unsuportes oprand type therefore I converted the type to int.
