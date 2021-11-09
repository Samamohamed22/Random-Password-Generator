
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("\nHow many letters would you like in your password? ")) 

nr_symbols = int(input(f"\nHow many symbols would you like? "))

nr_numbers = int(input(f"\nHow many numbers would you like? "))


print("")


password_List=[]

for L in range(nr_letters):
    password_List.append(random.choice(letters))
  

for S in range(nr_symbols):
    password_List.append(random.choice(symbols))
  

    
for N in range(nr_numbers):
    password_List.append(random.choice(numbers))


random.shuffle(password_List) #to randomize the order of the password list
print(password_List)

password=''

for charchters in password_List:
    password=password+charchters

print(f"\nyour password is : {password}") #to print the password inside the list as string of charachters 

