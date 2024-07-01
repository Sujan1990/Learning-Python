# fruits = []

# total_fruits = int(input("Enter total number of fruits: "))

# for i in range(1,total_fruits+1):
#     fruit_name = input(f"Enter fruit {i}")
#     fruits.append(fruit_name)
# print("Your fruits are: ")
# #Dispaly
# for fruit_name in fruits:
#     print(fruit_name)

fruits = []
total_fruits = int(input("Enter total number of fruits: "))

for i in range(1,total_fruits+1) : 
    fruit_name = input(f"Enter name of fruit {i}: ")
    fruits.append(fruit_name)
print("\n------Your Fruits are------")

#Display
for fruit_name in fruits:
    print(fruit_name)
