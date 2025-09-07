#Payroll with Overtime
hours = input("Enter hours: ")
rate = input("Enter rate: ")
fhours = float(hours)
frate = float(rate)
if fhours > 40:
    reg = fhours * frate
    otp = (fhours - 40) * (frate * 0.5)
    pay = reg + otp
else:
    pay = fhours * frate
print("Pay: ", pay)