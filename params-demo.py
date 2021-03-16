#1)(?) Write the function that finds the greater of the 2 numbers sent to it.

def comparison (a,b):
    if a>b:
        return "a>b less than a b."
    elif a<b:
        return "a<b greater than a b."
    return "a=b a is equal to b."
result = comparison(a=10,b=20)
print(result)


#2)(?) Find out how many times each character is repeated in a string of information sent to it.

def findthenumberofcharacters(string):
    return { letter: string.count(letter) for letter in string}
result = findthenumberofcharacters("flutter")
print(result)


#3)(?) Update the list according to the list, command, position and value information sent to it.

def updateList(list1, command, position, value=None):
    if command == "remove" and position == "end":
        return list1.pop()
    elif command == "remove" and position == "beginning":
        return list1.pop(0)
    elif command == "add" and position == "end":
        list1.append(value)
        return list1
    elif command == "add" and position == "beginning":
        list1.insert(0,value)
        return list1

result = updateList([1,2,3], "add" ,"end" ,4)
result = updateList([1,2,3], "add" ,"beginnig" ,4)
result = updateList([1,2,3], "remove" ,"beginning")
result = updateList([1,2,3], "remove" ,"end")


#4)(?) If there is "blue" in the color names sent to it, write the function that returns True.

def containsBlue(*args):
    if "blue" in args:
        return True
    else:
        return False

result = containsBlue("blue","black","yellow")
result = containsBlue("green","black","yellow")
