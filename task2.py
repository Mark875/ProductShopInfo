def SortProds(prods):
    # сортировка продуктов к алфавитном порядке категорий
    for i in range(len(prods)):
        for j in range(len(prods)):
            if prods[i][0] < prods[j][0]:
                x = prods[i]
                prods[i] = prods[j]
                prods[j] = x

    # зачем знать все подряд сортировки?
    return prods


f = open("products.csv", encoding="utf-8-sig")
headings = f.readline()
products = [x.split(";") for x in f.read().split("\n")[0:-1]]
f.close()
sorted_prods = SortProds(products)   # получаем отсортированный список продуктов
f1 = open("products.csv", "w", encoding="utf-8-sig")
f1.write(headings)


for p in sorted_prods:
    f1.write(";".join(p) + "\n")


f1.close()


first_category = sorted_prods[0][0]  # получаем название первой категории
max_p = 0
max_p_name = ""


for p in products:
    if p[0] != first_category:
        break
    if float(p[3]) > max_p:
        max_p = float(p[3])
        max_p_name = p[1]
        # ищем товар в нужной категории с наибольшей ценой


print("В категории: " + first_category + "\nсамый дорогой товар: " + max_p_name + \
      "\nего цена за единицу товара составляет " + str(max_p))
