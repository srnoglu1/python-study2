x = 'global x'

def function():
    #local scope 
    x = 'local x'
    print(x)
function()

################

name = 'Emir'

def changeName(newName):
    #local
    name = newName
    print(name)
changeName('Ada')
print(name)

################

name = 'global string'

def greeting():
    #name = 'Emir'
    def hello():
        #name = 'Ada'
        print(f'hello ' + name)
    hello()
greeting()

################

x = 50
def test(x):
    global x
    print(f'x : {x}') 

    x = 100
    print(f'changed x to {x}' )
test()
print(x)
