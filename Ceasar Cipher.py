# Ceasar Cipher

import os

from art import logo
from lists import alphabet, numbers


clear = lambda: os.system("clear")

def encoding(message, number):
    # Indeksowanie
    for i in message.lower():
        if i in alphabet:
            ind.append(alphabet.index(i))
        else:
            ind.append(0)
    # Powiekszanie indeksu o shift_number
    for i in ind:
        i += int(number)
        ind_new.append(i)
    # Tworzenie zakodowowanej wiadomosci
    for i in ind_new:
        mess_list.append(alphabet[i])
    mess = ""
    for i in mess_list:
        mess = mess + i
    return mess

def decoding(message, number):
    for i in message.lower():
        decode_i.append(alphabet.index(i))
    for i in decode_i:
        i -= int(number)
        decode_new_i.append(i)
    for i in decode_new_i:
        decode_mess_list.append(alphabet[i])
    mess = ""
    for i in decode_mess_list:
        mess = mess + i
    return mess

decode_mess_list = []
decode_new_i = []
decode_i = []
mess_list = []
ind = []
counter = 0
ind_new = []

flag = True
flag_2 = True
result = 0
while flag:
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if choice.lower() == "encode" or choice.lower() == "decode":  
        message = input("Type your message:\n")
        while flag_2:
            shift_number = input("Type the shift number:\n")
            if shift_number in numbers:    
                if choice == "encode":
                    result = encoding(message, shift_number)
                elif choice == "decode":
                    result = decoding(message, shift_number)
                print(f"Here's the encoded result: {result}!")
                break
            else: 
                continue
        next = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
        if next == "yes":
            continue
        else:
            flag = False
        print(f"Here's the decoded result: {result}")
    else:
        clear()
        continue
    if next.lower() == "no":
        flag = False
    
