list = []
list.append(5)
list.append(10)

# list = str(list)



print(list)

# my_list = [1, 2, 3]
# my_list[0] = 4  # my_list is now [4, 2, 3]
# my_list.append(5)  # my_list is now [4, 2, 3, 5]

test=str(list)

print(type(test))
print(test)

new_test = ''.join(test)
without_prefix = new_test.removeprefix("[")
without_suffix = without_prefix.removesuffix("]")
remove_space = without_suffix.replace(", ",'')

print(remove_space)

print(new_test[1])