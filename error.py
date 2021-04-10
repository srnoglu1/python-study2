try:
    ID = str(input("ID: "))
    PSW = int(input("PASSWORD: "))
    if str(ID):
        print("ID: ", ID)
    if int(PSW):
        print("PASSWORD: ", PSW)
    print("Entered values are successful.")
except:
    print("incorrect value entered.")

#

while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except (ZeroDivisionError,ValueError) as e:
        print('an error occorred.')
        print(e)
    except Exception as e:
        print('an uncnown error has occurred.')
        print(e)
    else:
        break
    finally:
        print('finally block worked.')
    
