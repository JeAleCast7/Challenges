# Write code below 💖

menu = [
  '#1 🍔 Cheeseburger',
  '#2 🍟 Fries',
  '#3 🥤 Soda',
  '#4 🍦 Ice Cream',
  '#5 🍪 Cookie'
]

def welcome(message):
  return message
print(welcome("Welcome to Burger King, What can I get you?"))
print(welcome("-----------MENU----------"))
print(welcome("#1 🍔 Cheeseburger"))
print(welcome("#2 🍟 Fries"))
print(welcome("#3 🥤 Soda"))
print(welcome("#4 🍦 Ice Cream"))
print(welcome("#5 🍪 Cookie"))

item = int(input("Ready to order: "))
def get_item(x):
  return menu[x-1]
print(get_item(item))