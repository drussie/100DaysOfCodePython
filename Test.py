# import random

# random_integert = random.randint(1, 10)
# print(random_integert)

# random_float = random.random() * 5 # 0.0000000 - 4.9999999
# print(random_float)

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america [2])
print(states_of_america [1])
print(states_of_america [-1])   # Last itme in the list
states_of_america[1] = "Pencilvania"
print(states_of_america [1])
states_of_america.append("Ondruskavania")
print(states_of_america)
states_of_america.extend(["Drakeland", "Czechoslovakia", "Jack Bauer land"])
print(states_of_america)


fruits = ["Apple", "Peach", "Pear"]
vegetables = ["Spinach", "Kale", "Tomatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(len(dirty_dozen))
print(dirty_dozen[1][1])

# Grid game
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
print("Enter a, b, or c for the row and 1, 2, or 3 for the column.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
spot_letter = position[0].upper()
num1 = 0
if spot_letter == "A":
  num1 = 0
elif spot_letter == "B":
  num1 = 1
else:
  num1 = 2

spot_number = int(position[1])
map [spot_number-1] [num1] = "X"


# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")

sum = 0
for number in range(1, 101):
    sum += number
print(sum)    

# Only add the even numbers
print("Enter a number")
target = int(input()) # Enter a number between 0 and 1000
sum = 0
for number in range(2, target + 1, 2):
    sum += number

print(sum)

# function
def three_prints(name):
  print(f"Hello {name}")
  print("three_prints")
  print("function on display")

three_prints("Marcos")

# functions iwth more than one input
def greet(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

greet("Marcos", "Prague")  
greet(location="Prague", name="Marcos")