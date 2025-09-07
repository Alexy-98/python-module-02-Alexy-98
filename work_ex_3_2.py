#Payroll with Error Input
hours = input("Enter hours: ")
rate = input("Enter rate: ")
try:
    fhours = float(hours)
    frate = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

print(fhours, frate)
if fhours > 40:
    reg = fhours * frate
    otp = (fhours - 40) * (frate * 0.5)
    pay = reg + otp
else:
    pay = fhours * frate
print("Pay: ", pay)