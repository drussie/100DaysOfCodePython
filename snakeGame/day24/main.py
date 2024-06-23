# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# Manage file.close automatically
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# Delete previous content and write new content
with open("my_file.txt", mode="w") as file:
    file.write("New text")    

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# Append new content to the file
with open("my_file.txt", mode="a") as file:
    file.write("\nHello, my name is Marcos.\nThis is the greatest thing ever.I love to play sports.\n")

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)    