# Write code below 💖
import random

my_numbers = []
winning_numbers = []

#My Numbers Generator
for i in range(0,5):
  my_numbers.append(random.randint(1, 69))
  
my_numbers.append(random.randint(1, 26))

#Lotterys number Generator
for i in range(0,5):
  winning_numbers.append(random.randint(1, 69))

winning_numbers.append(random.randint(1 , 26))

print('My numbers: ',my_numbers)
print('Winning Numbers: ',winning_numbers)