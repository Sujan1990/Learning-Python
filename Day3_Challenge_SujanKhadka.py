#Use of data type list for displaying example
First_Name = ["Sujan", "Asmita"]
Last_Name = ["Khadka", "Sharma"]
Age = [34, 33]
Address = ["Nepal", "USA"]

#Display example
print(f"example 1: {First_Name[0]} {Last_Name[0]} aged {Age[0]} lives in {Address[0]}.")
print(f"example 2: {First_Name[1]} {Last_Name[1]} aged {Age[1]} lives in {Address[1]}.")
print()
print("As above, please enter details of yourself and your friend so that the app can display it clearly for you to view")

#Requesting user input
print()
User_firstname = input(f"Enter your first name: ")
user_lastname = input(f"Enter your last name: ")
User_name = f"{User_firstname} {user_lastname}"
User_age = input(f"Enter your age: ")
User_address = input(f"Enter your address: ")
print()

print("Now enter your friends details")

friends_firstname = input(f"Enter your friends first name: ")
friends_lastname = input(f"Enter your friends last name:")
friends_name = f"{friends_firstname} {friends_lastname}"
friends_age = input(f"Enter your friends age: ")
friends_address = input(f"Enter your friends address: ")
print()

#Display user input data
print(f"{User_name} aged {User_age} lives in {User_address}")
print(f"{friends_name} aged {friends_age} lives in {friends_address}")
print()

#Counting length
print("Interesting fact")
print(f"Your name lenght is {len(User_name)}")
print(f"Your friends name length is {len(friends_name)}")
print("THE END")

