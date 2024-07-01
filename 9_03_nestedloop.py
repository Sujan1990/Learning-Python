start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for i in range (start,end+1):
    print(f"\nTABLE OF {i}\n")
    for j in range (1,11):
        print (f"{i} X {j} = {i*j}")
    print("-----------------")