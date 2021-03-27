numbers = [1,6,3,-5,4,9]
str_number = ["1", "3", "4" , "7", "9"]
name = ["Aslı", "Merve", "Emir", "cenk", "kerem"]

result = list(map(lambda x: x **2, numbers))
result = list(map(int, str_number))
result = list(map(abs, numbers))
result = list(map(float, numbers))
result = list(map(len, name))
result = list(map(str.capitalize, name))
result = list(map(str.lower, name))
print(result)


multiPlay = lambda x: x**2
result = multiPlay(5)

total = lambda a,b,c: a+b+c
result = total(5,6,7)
