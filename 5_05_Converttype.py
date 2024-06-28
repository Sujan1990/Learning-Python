number1 = input("Enter number 1: ")
number2 = input("Enter number 2: ")

sum = number1+number2

print(f"The string sum is {sum}")

# as above number is considered as string we do not get addition rather adjoinment of strings
# to add the given numbers it must be converted to integers by using int syntax
# we can use number1 = int(intput("Enter..."))
#or use in in sum function also
# or create new variables as follows

# number3=int(number1)
# number4=int(number2)



sum_int = int(number1)+int(number2)

print(f"The actual int sum is {sum_int}")

