#1. No parameter, No return

def one():
    print("Function type one: No parameter and no return.")

one()

#2. Parameter, No Return

def two(n1,n2):
    print(n1+n2)
print("Function type two: Parameter and no return.")
two(2,2)

# No Parameter and return 

def three():
    age = 18
    return age

print("Function type three: No parameter and return.")
ram_age = 16

if ram_age > three():
    print(f"Ram is {ram_age} years old and eligible to vote.")
else:
    print(f"Ram is {ram_age} years old and is not eligible to vote.")


# Parameter and return 

def multiplication(n1,n2):
    mult = n1*n2
    return mult

print("Function type four: Parameter and return.")
mult = multiplication(2,2)
print(f"The multiplication is {mult}.")