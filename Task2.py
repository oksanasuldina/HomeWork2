my_list = []
len_list = int(input('введите количество елементов списка: '))
i = 0
while i < len_list:
    my_list.append(input('введите {}-й элемент списка: '.format(i)))
    i += 1
print('введенный список: {} '.format(my_list))
for ind, el in enumerate(my_list):
    if ind % 2 == 0 and len_list % 2 == 0:
        my_list[ind], my_list[ind + 1] = my_list[ind + 1], my_list[ind]
    elif ind % 2 == 0 and len_list % 2 != 0:
        if ind != len_list - 1:
            my_list[ind], my_list[ind + 1] = my_list[ind + 1], my_list[ind]
        else:
            break
    else:
        continue
print('измененный список: {} '.format(my_list))
