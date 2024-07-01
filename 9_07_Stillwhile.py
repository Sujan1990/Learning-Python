atm_pin = '1234'

user_pin = ''

attempt = 0

while atm_pin != user_pin:
    if attempt > 0:
        print(f"Invalid Pin. Attempt {attempt}")
    user_pin = input("Enter your pin: ")
    attempt = attempt+1

print("Access granted. Enter withdrawal amount.")