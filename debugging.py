import pdb

one = "one"
two = "two"
pdb.set_trace()
result = one + two

three = "three"

result += three

print(result)

def add_numbers(a,b,c):
    import pdb; pdb.set_trace()
    return a+b+c

add_numbers(1,2,3)

# l => list
# n => next line
# p => print
# c => continue
