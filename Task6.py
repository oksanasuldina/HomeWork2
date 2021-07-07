products = []  # структура "Товары"
characteristics_products = ['название', 'цена', 'количество', 'eд']
names_products = []
costs_products = []
counts_products = []
units_products = []
count = int(input('введите количество товаров: '))
i = 0
while i < count:
    names_products.append(input('введите название {} товара: '.format(i + 1)))
    costs_products.append(input('введите цену {} товара: '.format(i + 1)))
    counts_products.append(input('введите количество {} товара в ассортименте: '.format(i + 1)))
    units_products.append(input('единица измерения {} товара ? введите, например, шт, г, л, кг '.format(i + 1)))
    dict_parameters = {characteristics_products[0]: names_products[i]}
    dict_parameters_2 = {characteristics_products[1]: costs_products[i]}
    dict_parameters_3 = {characteristics_products[2]: counts_products[i]}
    dict_parameters_4 = {characteristics_products[3]: units_products[i]}
    dict_parameters.update(dict_parameters_2)
    dict_parameters.update(dict_parameters_3)
    dict_parameters.update(dict_parameters_4)
    product_tuple = (i + 1, dict_parameters)
    products.insert(i, product_tuple)
    i += 1
print()
print('Структура данных "Товары"')
for el in products:
    print(el)
analytic_products = {characteristics_products[0]: names_products}
analytic_products_cost = {characteristics_products[1]: costs_products}
analytic_products_count = {characteristics_products[2]: counts_products}
analytic_products_unit = {characteristics_products[3]: list(set(units_products))}
analytic_products.update(analytic_products_cost)
analytic_products.update(analytic_products_count)
analytic_products.update(analytic_products_unit)
print()
print('Аналитика о товарах')
print(analytic_products)
