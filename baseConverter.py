from Stack import Stack

def baseConverter(num,base):
    # num is a number in decimal system
    # base is a basis of the new system 

    digits = '0123456789ABCDEF'
    remstack = Stack()

    while num > 0:
        rem = num % base
        remstack.push(rem)
        num = num // base

    newString = ''
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

print(baseConverter(24,2))
print(baseConverter(10,16))



# baseConverter is a function to convert numbers in the decimal system 
# to any other from to binary and hexadecimal system