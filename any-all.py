numbers = [0,1,3,5,9,6,10,8]

result = any(number for number in numbers)
result = all(number for number in numbers)
result = any([number for number in numbers if number2%==1])


persons = ["ali","ahmet","mehmet"]

result = any([persons[0]=='a' for person in persons])
result = all([persons[0]=='a' for person in persons if person[0=='a']])


print(result)
