import random

# random_number = random.randint(1,100)

# print(random_number)


# for i in range(1,6):
#     random_number=random.randint(1,100)
#     print(random_number)



alphabet = ' a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,'
alphabet_upper = alphabet.upper()
number = '1,2,3,4,5,6,7,8,9,0,'
symbols = '!,@,#,$,%,^,&'

combine = alphabet+alphabet_upper+number+symbols
combine_split = combine.split(",")



def password_generator(n1):
    password = []
    for i in range (1,n1+1):
        random1=random.choice(combine_split)
        password.append(random1)
    password_join = ''.join(map(str,password))
    print(password_join)

n1 = int(input("Enter length of required password: "))
password_generator(n1)






# def password_generator():
#     pass_list =[]
#     for i in range(1,31):
#         random_pass=random.choice(combine_split)
#         pass_list=pass_list.append()
#     return pass_list

# password = password_generator()

# print(password)

# number = []

# for i in range (1,11):
#     n=random.randint(1,100)
#     number.append(n)

# print(number)