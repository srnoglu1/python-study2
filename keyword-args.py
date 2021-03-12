def fullName(firstname,lastname):
   return f"your name {firstname} {lastname}"
result = fullName("Emirhan","Sirinoglu")
print(result)


lists =[10+20+30]
def total(numbers):
    result = 0
    for i in numbers:
        numbers =+ i
    return result
print(lists)


lists = []
def total(*args):
    result = 0
    for i in args:
        result =+ i
    return result
print(total(10+50-10))
