numbers = [34,2,5,7,98]

result = sum(numbers)
result = sum(numbers, 10)


products = [
    {"title":"iphone x", "price": 5000},
    {"title":"iphone xr", "price": 6000},
    {"title":"iphone 11", "price": 7000},
    {"title":"iphone 11 Pro", "price": 0},
]

# totalPrice = sum([urun["price"] for product in products])
# result = totalPrice / len(products)

totalPrice = sum([product["price"] for product in products])
numberOfProducts = len([product for product in products if product["price"]>0])
result = totalPrice / numberOfProducts

result = round(10.2)
result = round(10.6)
result = round(10.5)
result = round(1.424242, 2)
result = round(1.426242, 2)
result = round(1.426242, 4)

print(result)
