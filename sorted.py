numbers = [1,6,8,4,3,99,52]

result = sorted(numbers)
result = sorted(numbers ,reverse=True)


users = [
    {"username": "emirhan", "tweets": ["tweets 1", "tweets 2", "tweets 3"], "email": "ertek@info.com"},
    {"username": "selim", "tweets": ["tweets 1"]},
    {"username": "mert", "tweets": ["tweets 1", "tweets 2"], "name": "", "phone": "13546984223"} 
]

result = sorted(users, key=len)
result = sorted(users, key=len, reverse=True)
result = sorted(users, key=lambda user: ["email"])
result = sorted(users, key=lambda user: len(user["tweets"]))
result = sorted(users, key=lambda user: len(user["tweets"]))

print(result)


courses = [
    {"title": "Python course", "price":5000},
    {"title": "Java course", "price":8000},
    {"title": "C# course", "price":7000}
]

result = sorted(courses, key=lambda c: c["title"])
result = sorted(courses, key=lambda p: p["price"],reverse=True)
result = map(lambda c: c["title"],sorted(courses, key=lambda course: course["price"],reverse=True))


print(list(result))
