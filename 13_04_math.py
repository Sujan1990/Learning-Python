import math

def roundoff():
    user_input = float(input(f"Enter number: "))
    round_off = round(user_input)
    print(f'Round number is {round_off}')


# roundoff()


n1 = 3.1545678
print(f"The acutal number is {n1}")

print(f"Decimal with :.2f format is is {n1:.2f} ")

print(f"ceiing of number is {math.ceil(n1)}")
print(f"floor of number is {math.floor(n1)}")
print(f"2 to the power 3 is {math.pow(2,3)}")


