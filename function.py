def calculateAge(birthyear):
    return 2021 - birthyear

def howLongIsYourRetirementAge(birthyear,name):
    age = calculateAge(birthyear)
    remainingTime = 65 - age

    if (age>0):
        print(f'{name}, to retirement {remainingTime} year left.')
    else:
        print(f'{name}, already {remainingTime} you are retired.')

howLongIsYourRetirementAge(1998,"Emirhan")
print(howLongIsYourRetirementAge)
