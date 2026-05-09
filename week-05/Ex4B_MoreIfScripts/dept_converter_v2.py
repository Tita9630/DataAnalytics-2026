department_code = 12
match department_code:
    case 1:
        print("Marketing")
    case 5:
        print("Human Resources")
    case 10:
        print("Accounting")
    case 12:
        print("Legal")
    case 18:
        print("IT")
    case 20:
        print("Customer Relations")
    case _:
        print("Error")

    
# After comparing if/elif/else and match, I prefer using match since it is easier to read and to write the code too.