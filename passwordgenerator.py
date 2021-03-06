#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
level  = input("what level of difficulty would you like ? Easy or Hard\n")

#Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
if level == "Easy":    
    passwordeasy = ""
    for char in range(0, nr_letters):
        passwordeasy += random.choice(letters)

    for sym in range(0, nr_symbols):
        passwordeasy += random.choice(symbols)

    for int in range(0, nr_numbers):
        passwordeasy += random.choice(numbers)

    print(passwordeasy)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
elif level == "Hard":
    password_list = []

    for char in range(0, nr_letters):
        password_list += random.choice(letters)

    for sym in range(0, nr_symbols):
        password_list += random.choice(symbols)

    for int in range(0, nr_numbers):
        password_list += random.choice(numbers)


    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    print(password)
