pay_rate = 80
hours_worked = 45
filing_status = "joint"
if hours_worked > 40:
   overtime = hours_worked - 40 
   gross_salary = (40 * pay_rate) + (overtime * pay_rate * 1.5)
   print("Over 40 hours")
else:
   gross_salary = hours_worked * pay_rate

annual_gross_salary = gross_salary * 52

if filing_status == "single":
     if annual_gross_salary < 12000:
         tax_rate = 0.05
     elif annual_gross_salary < 25000:
         tax_rate = 0.10
     elif annual_gross_salary < 75000:
         tax_rate = 0.15
     else:
         tax_rate = 0.20


if filing_status == "joint":
     if annual_gross_salary < 12000:
         tax_rate = 0.00
     elif annual_gross_salary < 25000:
         tax_rate = 0.06
     elif annual_gross_salary < 75000:
         tax_rate = 0.11
     else:
         tax_rate = 0.20

tax_withheld = gross_salary * tax_rate
net_salary = gross_salary - tax_withheld

print(f"You worked {hours_worked} hours this period.")
print(f"Because you earn $ {pay_rate} per hour, your gross weekly pay is $ {gross_salary}")
print(f"Your filing status is {filing_status}")
print(f"Your tax withholding for the week is $ {tax_withheld}")
print(f"Your net pay is $ {net_salary}")