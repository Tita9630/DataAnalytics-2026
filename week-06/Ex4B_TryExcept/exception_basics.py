# ValueError =  when there is a wrong value in a specified data type
try:
    tea = int("water")
except ValueError:
    print("ValueError: You can't change a str to numbers")
else:
   print(tea)
finally:
   print("Let's try again")

# NameError = when a variable doesn't exist
try:
 m = Cookies
except NameError:
 print("NameError: Oops, I guess you forgot to assign an undefined object to a variable")
else:
 print(m)
finally:
 print("Let's try again")

# TypeError: when two different types are combined
 try:
    tea = "water" + 12
 except TypeError:
    print("TypeError: You can't add words to numbers")
 else:
   print(tea)
 finally:
   print("Let's try again")

# SyntaxError = when a syntax error occurs
try:
    tea = "water" + 12
 except TypeError:
    print("TypeError: You can't add words to numbers")
 else:
   print(tea)
 finally:
   print("Let's try again")

