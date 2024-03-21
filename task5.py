f_in = open("products.csv", "r", encoding="utf-8-sig")   # открываем файл
products = [x.split(";") for x in f_in.read().split("\n")[1:-1]]   # считываем информацию из файла
f_in.close()  # закрываем файл
table = []


for p in products:
    table.append((p[0], p[4]))
    # добавляем в таболицу нужную информацию о каждом продукте


table.sort(key=lambda x: float(x[1]))  # сортируем по возрастанию числа продаж


for i in table[:11]:
    print(i[0] + ", " + i[1])
    # выводим информацию о первых 10 продуктах
