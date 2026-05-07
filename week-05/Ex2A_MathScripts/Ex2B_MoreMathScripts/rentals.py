tourists = 38
van_seat = 15
van_cost = 250

van_needed = tourists // van_seat
remainder = tourists % van_seat

if remainder > 0:
    van_needed = van_needed + 1

total_van_cost = van_cost * van_needed
cost_per_person = total_van_cost / tourists


print(f"cost per person is {cost_per_person:.2f}")

collected_money = 19.74 * tourists
print(f"The collected money is {collected_money:.2f}")

print(f"The total cost of the vans is {total_van_cost:.2f}")

# I have a leftover of 0.12 because of rounding the decimal. Each person
# paid 19.74, while the exact amount we find when we divide 750 by 38 is 
# 19.736842105, and when we multiply 19.74 by 38, it gives us 750.12. 