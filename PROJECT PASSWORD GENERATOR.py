#CREATE A PASSWORD GENERATOR

import random

global password
global password_list


def easy_password():
    password = ''
    for i in range(0,no_of_letters):
        password = password+ random.choice(letters)
        
    for i in range(0,no_of_numbers):
        password += random.choice(numbers)
        
    for i in range(0,no_of_symbols):
       password += random.choice(symbols)
       
    return password

def hard_password():
    password_list = []
    password = ''
    for i in range(0,no_of_letters):
        password_list.append(random.choice(letters))
        
    for i in range(0,no_of_numbers):
        password_list.append(random.choice(numbers))
        
    for i in range(0,no_of_symbols):
       password_list.append(random.choice(symbols))
       
    #shuffling the list - reordering the list
    
    random.shuffle(password_list)
    for i in range(0,len(password_list)):
        password += password_list[i]
        
    return password


print("Welcome to PyPassword Generator!")

no_of_letters = int(input("How many letters would you like in your password? "))
no_of_numbers = int(input("How many numbers would you like? "))
no_of_symbols = int(input("How many symbols would you like? "))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

difficulty_level = input("Would you like an easy password or a hard one? Type 'easy' or 'hard': ")


if difficulty_level == 'easy':
    print(f"Your easy password is: {easy_password()}")
    
else:
  print(f"Your hard password is: {hard_password()}")  










