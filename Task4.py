str_use = input('введите строку из нескольких слов, разделённых пробелами: ')
str_use_list = list(str_use.split())
for ind, el in enumerate(str_use_list):
    if len(str_use_list[ind]) < 10:
        print(ind + 1, el)
    else:
        print(ind + 1, el[0:10:1])
