# 1)(?) Give Turkish character error in entered characters.


def checkPassword(password):
    turkish_characters = "şçğüöıİ"

    for i in password:
        if i in turkish_characters:
            raise TypeError("The password cannot contain Turkish characters.")

    print("successful password.")

password = input("password: ")

try:
    checkPassword(password)
except TypeError as e:
    print(e)


# 2)(?) Create the factorial function and give error messages for the value that comes to the function.

def factorial(x):
    x = int (x)

    if (x<0):
        raise ValueError ("Ngative value.")
    result = 1
       
    for i in range(1, x+1):
        result *=i
      
    return result
        
for i in [5,7,4,"a",6,"14b",-2,9]:
    try:
        x = factorial(i)
    except ValueError as e:
        print(e)
        continue
    else:
        print(x)
