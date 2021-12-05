import random


def shuffle(string):
    templist = list(string)
    random.shuffle(templist)
    return ''.join(templist)


uppercaseLetter1 = chr(random.randint(65, 90))

uppercaseLetter2 = chr(random.randint(65, 90))

lowercaseLetter1 = chr(random.randint(97, 122))

lowercaseLetter2 = chr(random.randint(97, 122))

number1 = chr(random.randint(48, 57))

number2 = chr(random.randint(48, 57))

symbol1 = chr(random.randint(33, 47))

symbol2 = chr(random.randint(33, 47))

password = symbol1 + symbol2 + number1 + number2 + lowercaseLetter1 +\
           lowercaseLetter2 + uppercaseLetter1 + uppercaseLetter2

password = shuffle(password)
print(password)
