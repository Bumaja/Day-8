# Ceasar Cipher

import os

from art import logo
from lists import alphabet, numbers
from decode import decoding
from encode import encoding

clear = lambda: os.system("clear")

flag = True
flag_2 = True
result = 0

print(logo)
while flag:
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if choice.lower() == "encode" or choice.lower() == "decode":  
        message = input("Type your message:\n")
        while flag_2:
            shift_number = int(input("Type the shift number:\n"))
            if shift_number in range(0, 52):    
                if choice == "encode":
                    result = encoding(message, shift_number)
                    print(f"Here's the encoded result: {result}!")
                elif choice == "decode":
                    result = decoding(message, shift_number)
                    print(f"Here's the decoded result: {result}")
                break
            else: 
                continue
        next = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
        if next == "yes":
            continue
        else:
            flag = False
    else:
        clear()
        continue
    if next.lower() == "no":
        flag = False
    
