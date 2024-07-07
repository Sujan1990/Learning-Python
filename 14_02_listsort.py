#Concerning Lists
import random

names = ['Sujan', 'Suman', 'Ram']


names.append('Hari')
names.append('Shyam')
names.append('Anuj')
names.append('Bimal')

names.sort()
names.reverse()

for i in names:
    print(i)

print(random.choice(names))

num = names.index('Sujan')
print(num)

#OR

print(names.index('Anuj'))

