#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:

u = nr_letters + nr_numbers + nr_symbols

a = random.sample(letters,nr_letters)

b = random.sample(numbers,nr_numbers)

c = random.sample(symbols,nr_symbols)
x = a+c+b
combined = "".join(x)
print("*******************\n")
print(f"Your eazy password: {combined}\n")

#Hard Level - Order of characters randomised:

hard =[]
for i in range(1, nr_letters+1):
  hard.append(random.choice(a))
for h in range(1,nr_numbers+1):
  hard.append(random.choice(b))
for k in range(1,nr_symbols+1):
  hard.append(random.choice(c))

random.shuffle(hard)
hard_combined = "".join(hard)
print("*******************\n")
print(f"Your hard level password: {hard_combined}")