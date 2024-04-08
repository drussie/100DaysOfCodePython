import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(text, shift, direction):
    new_text = ""
    for char in text:
        if char not in alphabet:
            new_text += char
            continue
        position = alphabet.index(char)
        if direction == "encode":
            new_position = (position + shift) % len(alphabet)
        else:
            new_position = (position - shift) % len(alphabet)
        new_letter = alphabet[new_position]
        new_text += new_letter
    print(f"The {direction}d text is {new_text}")

print(art.logo)
print("Welcome to the Caesar Cypher")

end = ""
while end != "no":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))  

    caeser(text, shift, direction)  

    end = input("Do you want to continue? Type 'yes' or 'no':\n").lower() 
    if end == "no":
        print("Goodbye!")

       
