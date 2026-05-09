pay_rate = 70
hours_worked = 40
if hours_worked > 40:
   overtime = hours_worked - 40 
   gross_salary = (40 * pay_rate) + (overtime * pay_rate * 1.5)
   print("Over 40 hours")
else:
   gross_salary = hours_worked * pay_rate
   if hours_worked < 40:
      print("Under 40 hours")
   else:
      print("Exactly 40 hours")
print(f"Gross salary is {gross_salary}")