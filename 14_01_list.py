#Concerning Lists

names = ['Sujan', 'Suman', 'Ram']

for name in names:
    print(name)

names.append('Hari')
names.append('Shyam')
names.append('Shyam')

for name in names:
    print(f"--{name}--")

count_Shyam = names.count('Shyam')
print(count_Shyam)

names.pop()

print(names)

# names.clear()



for name in names:
    print(f"--{name}--")