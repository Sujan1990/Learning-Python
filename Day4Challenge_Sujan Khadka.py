# Add your electricity bill from Jan to Dec in dictionary and find total and average

Electricity_Bill = {
    'jan' : 200,
    'feb' : 150,
    'mar' : 120,
    'apr' : 120,
    'may' : 120,
    'jun' : 150,
    'jul' : 150,
    'aug' : 120,
    'sep' : 120,
    'oct' : 120,
    'nov' : 120,
    'dec' : 200,

}

total=sum(Electricity_Bill.values())


print(Electricity_Bill.values())
print(f'Total electricity bill is {total}')
print(f'Average electricity bill is {total/7}')
