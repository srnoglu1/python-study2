ages = [2,5,7,16,18,25,33,46]

def adult(x):
    if x<18:
        return False
    else:
        return True

result = filter(adult,ages)
result = list(filter(lambda x: x>=18 ,ages))


numbers = [15,35,48,96,3,47,11]

result = list(filter(lambda n: n %2 == 0 ,numbers))


name = ["mustafa","sena","burak","cansu","mert"]

filteredResult = filter(lambda n: n[0]=="m", name)
result = list(map(lambda n: n.upper(), filteredResult))


users = [
    {"username": "mertalaska", "tweets": ["tweets1", "tweets2","tweets3"]},
    {"username": "senaalaska", "tweets": ["tweets1", "tweets2"]},
    {"username": "buraktemel", "tweets": []},
    {"username": "cansutopal", "tweets": ["tweets1"]}
]

result = list(filter(lambda t: len(t["tweets"])>0, users))
result = list(map(lambda t: t["username"].upper(), users))
print(result)
