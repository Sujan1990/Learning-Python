todo_list = ["Lear to code","Read Book","go to gym","Meditate"]

# print(f"{todo_list}")
# print(todo_list)
# print(todo_list[0])
# print(todo_list[1])
# print(todo_list[2])

#append is used to add
todo_list.append("go to gym")
# todo_list.clear()

#to add
todo_list[4] = "revise data test"

#pop: to remove last item
# todo_list.pop() 

for todo in todo_list:
    print(todo)

print(type(todo_list))