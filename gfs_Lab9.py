# Gavin Strickland

menu_option = 0

def encode(string):
    output = ""
    for i in string:
        output += str(int(i) + 3)
    return output

while menu_option != 3:
    print("Menu:\n1. Encoder\n2. Decoder\n3. Exit")
    menu_option = int(input("What would you like to do? "))
    if menu_option == 1:
        encode_str = input("Input string to be encoded: ")
        print("Your password has been encoded and stored!\n")
    if menu_option == 2:
        decode_str = decode(encode_str)
print("Goodbye!")