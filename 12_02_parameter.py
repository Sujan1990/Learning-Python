
## WAP to print even number between start yo end using function

def display_even(start,end):
    for i in range(start,end):
        if i % 2 == 0:
            print(i)


start = int(input("Enter start: "))
end = int(input("Enter end: "))

print(f"\nEven numbers between {start} and {end} are: ")
display_even(start,end)


# def displayeven(start, end):
#     for i in range(start,end):
#         if i % 2 == 0:
#             print(i)

# ()




