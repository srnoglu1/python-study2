def displayUser(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')
    print('\n')
displayUser(username = 'emirhan')
displayUser(username= 'emirhan', gmail = 'srnoglu98@gmail.com')
displayUser(username= 'emirhan', gmail = 'srnoglu98@gmail.com', country = 'Turkey')

def myFunch(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
myFunch(10,20,30,40,50,key1 = 'value1',key2 = 'value2')
