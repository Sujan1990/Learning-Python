
def reversename():
    name = str(input("Enter name to reverse: "))
    reverse=''
    # length=len(string)
    for i in range(0,len(name)):
        reverse = reverse + name[len(name)-1-i]
        # print(name[len(name)-1-i])
    print(reverse)


reversename()



def reverse_string(text):
    name = text
    reverse_string = ""
    for i in range(len(name)-1, -1, -1):
        reverse_string = reverse_string + name[i]
    print(f"Reverse is {reverse_string}")