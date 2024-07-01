#Create program that asks user to enter n number of todo and displays the same
todos = []

total_todo = int(input("Enter total number of todo: "))

for i in range (1,total_todo+1):
    list_todo = input(f"Enter todo {i} : ")
    todos.append(list_todo)

print("\n-------------------\nAll todos are: \n")
#Display result
for list_todo in todos:
    print(list_todo)
print("\n")