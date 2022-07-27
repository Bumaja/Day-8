# Ceasar Cipher

import os

from ceasar import ceasar
from art import logo
from lists import alphabet, numbers

clear = lambda: os.system("clear")

print(logo)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message.\n").lower()
    shift_number = int(input("Type the shift number.\n"))
    while shift_number > len(alphabet):
        shift_number = int(input(f"Type the shift number, smaller than {len(alphabet)}.\n"))
    ceasar(direction=direction, start_text=text, shift_number=shift_number)
    next = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if next == "no":
        break
    