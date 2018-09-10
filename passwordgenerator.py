import random
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!@#$%^&*'

# how many passwords do you need
number = input('number of passwords?')
number = int(number)

# what is the length of the password
length = input('password length?')
length = int(length)

for p in range(number):
    password = ''
    # create the number of characters for the password
    for c in range(length):
        password += random.choice(chars)
    print(password)
