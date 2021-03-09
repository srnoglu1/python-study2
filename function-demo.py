#1)(?) Write a function that returns the integer divisors of a number sent to it in list format.

def findDivisors(number):
    divisors = []
    
    for x in range(2,number):
        if (number % x == 0):
            divisors.append(x)
    return divisors
print(findDivisors(15))


#2)(?) Write the function that shows a word sent to it on the screen for the specified time.

def toPrint(txt, piece):
    print(txt*piece)
toPrint("hello\n", 3)


#3)(?) Write the function that calculates the area and perimeter of the rectangle.

def calculate(short,long):
    area = (short*long)
    primeter = 2* (long+short)

    print(f'area: {area} primeter: {primeter}')
calculate(15,8)


#4)(?) Do the coin flip application by using the function. (Random module)

def frontBack():

    import random
    number = random.random()
    if number>0.5:
        print('front')
    else:
        print('back')
frontBack()


#5)(?) Write the function that finds all prime numbers between the 2 numbers sent to it.

def primeNumber(number1,number2):
    for number in range(number1,number2+1):
        if (number>1):
            for i in range(2,number):
                if (number % i == 0 ):
                    break
            else:
                print(number)    
print(primeNumber(10,20))       
