employee = [
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

selected_department = input("Please select a department whose workers' names you want to see: ")

Deptwise_names = [name[0] for name in employee if name[1] == selected_department]

if Deptwise_names:
    print(f"Employees in {selected_department} department: {', '.join(Deptwise_names)}")
else:
    print(f"No employees found in the {selected_department} department.")