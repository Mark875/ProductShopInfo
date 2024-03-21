def Find_info(category, prods):
    # ищет нужную информацию по заданной категории в списке продуктов
    min_sold = float("inf")
    name = ""
    for p in prods:
        if p[0] == category:
            if float(p[4]) < min_sold:
                min_sold = float(p[4])
                name = p[1]
    
    
    return (name, min_sold)


f = open("products.csv", encoding="utf-8-sig")
products = [x.split(";") for x in f.read().split("\n")[1:-1]]
f.close()
category = input("Введите название категории: ")

while category != "молоко":
    name, sold = Find_info(category, products)

    if name == "":
        print("Такой категории не существует в нашей БД")
    else:
        print("В категории: " + category + "\nтовар: " + name + \
              "\nбыл куплен " + str(sold) + " раз")

    category = input("Введите название категории: ")
