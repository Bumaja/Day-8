from lists import alphabet

def decoding(message, number):
    mess = ""
    for letter in message:
        position = alphabet.index(letter)
        new_position = position - number
        new_letter = alphabet[new_position]
        mess += new_letter
    return mess