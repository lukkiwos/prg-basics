import csv

file_name = "clothing.csv"

with open(file_name, 'r', encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)


    for row in reader:
        product_name = row[1]
        size = row[3]
        color = row[4]
        price = float(row[5])
        stock_quantity = int(row[6])

        if price < 60 and stock_quantity < 40:
            print(f"{product_name} {size} {color}, {price} {stock_quantity}")