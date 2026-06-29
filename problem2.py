def find_top_seller(products: dict, sales: dict) -> str:
    max_tushum = 0
    sotilgan = ""

    for p in products:
        tushum = products[p] * sales[p]

        if tushum > max_tushum:
            max_tushum = tushum
            sotilgan = p

    return sotilgan

print(find_top_seller(
    {"Olma": 5000, "Banan": 8000, "Uzum": 7000},
    {"Olma": 10,   "Banan": 5,    "Uzum": 8}
))