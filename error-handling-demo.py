list = ["10","23","6a","65","4c","52b","12"]

# 1)(?) Find the numerical values ​​in the list elements.

for l in list:
    try:
        result = int(l)
        print(result)
    except ValueError:
        continue


# 2)(?) Unless the user enters the 'quit (q)' value, each input
#Make sure it is #, otherwise write an error message.

while True:
    number = input("number: ")
    if number == "q":
        break
    
    try:
        result = float(number)
        print(f"entered number {result}")
        break   
    except ValueError:
        print("invalid number")
        continue


# 3)(?) Get (d, key), which takes the dictionary and key information as parameters
# Prepare the function.

product = {"product name": "Samsung A10", }

def get(d,key):
    try:
        return d[key]
    except KeyError:
        return None

print(get(product,"price"))
print(get(product,"product name"))





