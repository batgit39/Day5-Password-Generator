import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator")
users_letters = int(input("How many letters would you like in your password : "))
users_symbols = int(input("How many symbols would you like : "))
users_numbers = int(input("How many numbers would you like : "))


# this is the first method I used to complete the task and it works just fine, but I had to redo the task because I didn't use much of loops here
#r_letter = random.sample(letters, users_letters)
#r_symbols = random.sample(symbols, users_symbols)
#r_numbers = random.sample(numbers, users_numbers)

#pwd = r_numbers + r_symbols + r_letter
#total_char = users_letters + users_symbols + users_numbers
#random_password  = random.sample(pwd, total_char)

random_password = []

for i in range(0, users_letters):
    random_password += random.choice(letters)

for i in range(0, users_numbers):
    random_password += random.choice(numbers)

for i in range(0, users_symbols):
    random_password += random.choice(symbols)

random.shuffle(random_password)

final_password = ""

for i in random_password:
    final_password += i

print(f"{final_password}")
