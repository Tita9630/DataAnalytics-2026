year = 20212
if year % 400 == 0:
    print(f"{year} is a leap year")
elif year % 100 == 0:
    print(f"{year} is not a leap year")
elif year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# 1900 is not a leap year
# 1950 is not a leap year
# 1999 is not a leap year
# 2000 is a leap year
# 2001 is not a leap year
# 20212 is a leap year




