my_list = [7, 5, 3, 3, 2]
is_menu = 1
while is_menu != 0:
    new_el = int(input('введите новый элемент рейтинга: '))
    print('рейтинг до: {}'.format(my_list))
    if my_list.count(new_el) != 0:
        my_list.insert(my_list.index(new_el) + my_list.count(new_el), new_el)
        print('рейтинг после: {}'.format(my_list))
        is_menu = int(input('продолжить? да - 1, нет - 0 '))
    elif my_list.count(new_el) == 0:
        max_el = my_list[0]
        i = 1
        while i < len(my_list):
            if my_list[i] >= new_el + 1:
                max_el = my_list[i]
                i += 1
            else:
                break
        if new_el > max_el:
            my_list.insert(my_list.index(max_el), new_el)
            print('рейтинг после: {}'.format(my_list))
            is_menu = int(input('продолжить? да - 1, нет - 0 '))
        elif new_el < max_el:
            my_list.insert(my_list.index(max_el) + 1, new_el)
            print('рейтинг после: {}'.format(my_list))
            is_menu = int(input('продолжить? да - 1, нет - 0 '))



