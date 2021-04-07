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
