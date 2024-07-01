# atm_pin = '1234'

# user_pin = ''

# while atm_pin != user_pin:
#     user_pin = input("Enter ATM pin: ")

# 

atm_pin = '1234'

user_pin = ''
attempt = 0

while atm_pin != user_pin:
    if attempt>0:
        print(f"Invalid pin code. Attempt number {attempt}")
    user_pin = input("Enter ATM pin: ")
    attempt=attempt+1
print("Access Granted. \nEnter withdrawl amount.")
