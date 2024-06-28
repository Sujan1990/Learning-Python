# if there is key value then it is dictionary, if no key value then set
#Dict has key and value

expenses = {
    'Sunday' : 10,
    'Monday' : 10,
    'Tuesday' : 10,
    'Wednesday' : 10,
    'Thursday' : 10,
    'Friday' : 1,
    'Saturday' : 10,


}

print(type(expenses))
print(expenses.values())

total = sum(expenses.values())

print(f"Total expenses is {total}")
print(f"Average is {total/7}")

print(f"Friday expenses is {expenses['Friday']}")