def GeneratePromo(product):
    return product[1][:2].upper() + product[2].split(".")[0] + \
           product[1][-2:][::-1].upper() + product[2].split(".")[1][::-1]

f_in = open("products.csv", "r", encoding="utf-8-sig")
headings = f_in.readline().split("\n")[0]
products = [x.split(";") for x in f_in.read().split("\n")[:-1]]
f_in.close()

f_out = open("product_promo.csv", "w", encoding="utf-8-sig")
f_out.write(headings + ";promocode\n")


for p in products:
    f_out.write(";".join([p[0], p[1], p[2], p[3], p[4], GeneratePromo(p)]) + "\n")

f_out.close()
