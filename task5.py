f_in = open("products.csv", "r", encoding="utf-8-sig")
products = [x.split(";") for x in f_in.read().split("\n")[1:-1]]
f_in.close()
table = []


for p in products:
    table.append((p[0], p[4]))



table.sort(key=lambda x: float(x[1]))


for i in table[:11]:
    print(i[0] + ", " + i[1])
