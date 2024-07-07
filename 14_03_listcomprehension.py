numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = [x for x in numbers if x%2==0]

# print(even_numbers)


names =['Anish', 'BInod', 'Ratna', 'Suman', 'aryan', 'Bibek']



#Find all names that start with A

#Logic
# for name in names:
#     print(name[0])

# names_withA = []
# for i in names:
#     if i[0] == 'A':
#         names_withA.append(i)

#OR

names_withA = [x for x in names if x[0].lower() =='a']  # This looks for both capital and small a.

#OR

# names_withA = [name for name in names if name.startswith("A")]

for i in names_withA:    
    print(i)




