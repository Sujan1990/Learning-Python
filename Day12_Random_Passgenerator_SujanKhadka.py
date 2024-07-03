import random

alphabet = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,'
alphabet_upper = alphabet.upper()
number = '1,2,3,4,5,6,7,8,9,0,'
symbol = '!,@,#,$,%,^,&,'

combine = alphabet+alphabet_upper+number+symbol
combine_tolist = combine.split(",")

def password_generator(n1):
    password = []
    for i in range(1,n1+1):
        random1 = random.choice(combine_tolist)
        password.append(random1)
    password_join = ''.join(map(str,password))
    print(f'Your random password of length {n1} is: {password_join}')
    print("______THANK YOU______")

n1 = int(input("***ENTER LENGHT OF REQUIRED PASSWORD: "))
password_generator(n1)


    