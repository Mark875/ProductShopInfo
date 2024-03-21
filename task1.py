f_input = open("products.csv", "r", encoding="utf-8-sig")
f_output = open("products_new.csv", "w", encoding="utf-8-sig")
f_output.write(f_input.readline().split("\n")[0]+";Total\n")

products = [x.split(";") for x in f_input.read().split("\n")[:-1]]
summa = 0


for p in products:
    category, product, date, price, count = p[0], p[1], p[2], p[3], p[4]
    # получаем информацию по продукту
    total = float(price) * float(count)
    # считаем выручку
    f_output.write(";".join([category, product, date, price, count, str(total)]) + "\n")
    # записываем результат
    if category == "Закуски":
        summa += total
        # считаем выручку с закусок


f_input.close()
f_output.close()
#закрываем файлы
print(summa)
#выводим информацию по закускам