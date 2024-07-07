#Ask user to enter n number of people name and print all name start with B
# IF there is no name with B it should say no name found
## if there is name it should display. 

### defining universal variables.
names = []
user_input = []
name_alphabet = []

#Function to take name inputs
def ask_names():
    print("-------NAME MANAGEMENT SYSTEM--------")
    nummber_of_names = int(input("Enter total number of names you want to add: "))
    for i in range(1,nummber_of_names+1):
        name = input(f"Enter name {i}: ")
        names.append(name)

# Function to display total inputs
def print_total_names():
    print(f"\nThe total number of names you have entered are {len(names)} and the thier list is as follows:")
    for i in names:
        print(i)

#Function to sort name by user given input 
def name_startswith():
    print("-----SORT NAME BY STARTING ALPHABET-----")
    user_input = input("Choose an Alphabet: ")
    name_startswith_alphabet = [x for x in names if x[0].lower() == user_input.lower()]
    if len(name_startswith_alphabet) > 0:
            print(f"Below displayed are the names of people which starts with the alphabet {user_input}.")
            for i in name_startswith_alphabet:
                print(i)
                name_alphabet.append(name_startswith_alphabet)
            print("Thank you for your time. See your soon. ") 
    elif len(name_startswith_alphabet) == 0:
        print(f"Sorry there are no names starting with {user_input}.")

def try_again ():
    if len(name_alphabet) == 0:
        print("Would you like to try again")
        choice = input("Enter (Y) for Yes or (N) for No, (Y/N): ")
        if choice.lower() == 'y':
            name_startswith()
        elif choice.lower() == 'n':
            print("Thank you for your time. See your soon. ")    
    else:
        print("Thank you for your time. See your soon. ") 

#Calling functions
ask_names()
print_total_names()    
name_startswith()

#Try again 
if len(name_alphabet) == 0:
    try_again()






