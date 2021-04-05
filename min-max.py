numbers = [1,5,7,45,25,89]
letters = ['a','v','h','s']
names = ['ahmet','ismail','ada','sena','sadık']

result = min(numbers)
result = max(numbers)

result = min(letters)
result = max(letters)

result = min(names)
result = max(names)

result = min([len(name) for isim in names])
result = max([len(name) for isim in names])

result = max(names, key=lambda n: len(n))
result = min(names, key=lambda n: len(n))


products = [
    {"title":"iphone x","price":5000},
    {"title":"iphone xr","price":6000},
    {"title":"iphone 11","price":7000}
]

result = min(products, key=lambda product: product['price'])
result = min(products, key=lambda product: product['price'])['title']
result = max(products, key=lambda product: product['price'])['title']

print(result)
