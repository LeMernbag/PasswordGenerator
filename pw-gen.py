import random
import string

# Functions


def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)


def randChar(length=2):
    characters = '@#$%&!'
    return ''.join((random.choice(characters)) for i in range(length))


def randUpper(length=1):
    uppers = chr(random.randint(65, 90))
    return ''.join((random.choice(uppers)) for i in range(length))


def randLower(length=1):
    lowers = chr(random.randint(97, 122))
    return ''.join((random.choice(lowers)) for i in range(length))


def randDigit(length=1):
    digits = chr(random.randint(48, 57))
    return ''.join((random.choice(digits)) for i in range(length))


# generate random characters using above functions
uppercaseLetter1 = randUpper()
uppercaseLetter2 = randUpper()
lowercaseLetter1 = randLower()
lowercaseLetter2 = randLower()
digit1 = randDigit()
digit2 = randDigit()
specialChars = randChar()

# Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + \
    lowercaseLetter2 + digit1 + digit2 + specialChars
password = shuffle(password)

# Ouput
print(password)
