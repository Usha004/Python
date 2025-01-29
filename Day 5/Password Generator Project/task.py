letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Easy level:
password = ""
import random
# number of letters = 4
for char in range(1,nr_letters+1):
    #1 - 4
    random_char = random.choice(letters)
    password += random_char
 # number of numbers
for num in range(1,nr_numbers+1):
    random_num = random.choice(numbers)
    password += random_num
# number of symbols
for sym in range(1, nr_symbols+1):
    random_sym = random.choice(symbols)
    password += random_sym
# print(password)


#Hard_level;

password_list = []
import random
for char in range(1,nr_letters+1):
    random_char = random.choice(letters)
    password_list += random_char
for num in range(1,nr_numbers+1):
    random_num = random.choice(numbers)
    password_list += random_num
for sym in range(1, nr_symbols+1):
    random_sym = random.choice(symbols)
    password_list += random_sym
print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char
print(f"your password is: {password}")














