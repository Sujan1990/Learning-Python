#Finding biggest number

n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))
n3 = float(input("Enter number 3: "))


if n1 > n2 and n1 > n3 :
    print(f"{n1} is the biggest number")
elif n2 > n1 and n2 > n3 :
    print(f"{n2} is the biggest number")
elif n3 > n1 and n3 > n2 :
    print(f"{n3} is the biggest number")
else:
    print("something went wrong")

