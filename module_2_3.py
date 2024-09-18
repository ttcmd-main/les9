my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list):
    my_list_number = my_list[index]
    if my_list_number < 0:
        break
    elif my_list_number > 0:
        print(my_list_number)
    index += 1