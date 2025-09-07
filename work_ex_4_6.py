#Payroll with Compute Pay
def computepay(hours, rate):
    print("In computepay", hours, rate)
    if hours > 40:
        reg = hours * rate
        otp = (hours - 40) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate
    print("Returning", pay)
    return pay

hours = input("Enter hours: ")
rate = input("Enter rate: ")
fhours = float(hours)
frate = float(rate)

pay = computepay(fhours, frate)

print("Pay: ", pay)