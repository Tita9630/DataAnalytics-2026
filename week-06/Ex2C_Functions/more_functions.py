def display_mailing_label(name, address, city, state, zip):
    print(name)
    print(address)
    print(f"{city}, {state} {zip}")
display_mailing_label(
    "Luna", 
    "1314 bridge", 
    "florence", 
    "sc", 
    "20030"
)

def add_numbers(*numbers):
    result = sum(numbers)
    expression = "+".join(str(num) for num in numbers)
    print(f"{expression} = {result}")
    print()
add_numbers(10) # one number
add_numbers (10, 5) # two numbers
add_numbers(8, 4, 4, 2) # more than two numbers

def display_receipt(total_due, amount_paid):
    print(f"Total due: ${total_due}")
    print(f"Amount paid: ${amount_paid}")
    change_due = amount_paid - total_due

    if change_due > 0:
        print(f"Change due: ${change_due}")
    elif change_due == 0:
        print("Change due: $0")
    else:
        print(f"Remaining balance: ${abs(change_due)}")
    print()

display_receipt(50, 70) # overpay
display_receipt(80, 80) # exactpay
display_receipt(250, 200) # underpay

# Calling display mailing lable

display_mailing_label(
    "Luna", 
    "1314 bridge", 
    "florence", 
    "sc", 
    "20030"
)

display_mailing_label(
    "Dave John",
    "52 st",
    "charlotte",
    "Nc",
    "25022"
)

# Calling add_numbers
add_numbers(10) # one number
add_numbers (10, 5) # two numbers
add_numbers(8, 4, 4, 2) # more than two numbers

display_receipt(50, 70) # overpay
display_receipt(80, 80) # exactpay
display_receipt(250, 200) # underpay


def display_mailing_label_bonus(name, address1, city, state, zip, address2=""):
    print(name)
    print(address1)
    if address2 != "":
        print(address2)
    print(f"{city}, {state} {zip}")
display_mailing_label_bonus(
    "Luna", 
    "1314 bridge", 
    "florence", 
    "sc", 
    "20030"
    "Apartment 5A"


)

def display_receipt_bonus(amount_paid, *total_dues):
    total_due = sum(total_dues)
    print(f"Total due: ${total_due}")
    print(f"Amount paid: ${amount_paid}")
    change_due = amount_paid - total_due

    if change_due > 0:
        print(f"Change due: ${change_due}")
    elif change_due == 0:
        print("Change due: $0")
    else:
        print(f"Remaining balance: ${abs(change_due)}")
    print()

display_receipt_bonus(50, 70, 200) # overpay