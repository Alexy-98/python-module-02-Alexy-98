#Detailed Output for Largest of Three
def greatestofthree (num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1, "Num1"
    elif num2 >= num3:
        return num2, "Num2"
    else:
        return num3, "Num3"
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))
except ValueError:
    print("Error, please enter numeric input")

greatest, var_name = greatestofthree(num1, num2, num3)
#This is the key!

message = (
    f"You have entered {num1}, {num2}, and {num3}."
    f"The first number you entered was assigned a variable of {num1}, the second to {num2}, and the third to {num3}."
    f"Your input was processed and the largest number you entered was {greatest} "
    f"which belonged to the integer variable {var_name}."
)

print(greatestofthree(num1, num2, num3))
print(message)