employee = [
    #(name and department)
    ('Sujan Khadka', "Treasury"),
    ('Suman Khadka', "IT"),
    ('Aman Raj', "IT"),
    ('Raman Sharma', "Treasury"),
    ('Ram Ghimire', "Credit"),
    ('Hari Saranam', "IT"),
    ('Ravi Gautam', "Credit"),
    ('Shyam Gautam', "HR"),
    ('Hari Khadka', "HR"),
    ('Sridhar Kafle', "IT")
]

'''
Create a program which displays list of department to user and outputs name of employees working in specific department
choosen by user. 
'''

def unique_departments():
    Dept_name = [dept for dept in employee]
    Department_set = set()
    for i in Dept_name:
        Department_set.add(i[1])
    Department_name_tuple = tuple(Department_set)
    return (Department_set)

print("------The list of departments are------")
for i in unique_departments():
    print (i)
print("---------------------------------------")

user_input = input("Please select a department whoese workers name you want to see: ")

emp_name = [name for name in employee if name[1] == user_input]

if emp_name:
    print(f"Employees working in {user_input} are: ")
    for i in emp_name:
        print(i[0])
else:
    print(f"No employees working in {user_input}")



