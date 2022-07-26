from lists import alphabet
def ceasar(start_text, shift_number, direction):
    text = ""
    if direction == "decode":
            shift_number *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            position = position + shift_number
            text = text + alphabet[position]
        else:
            text = text + char

    print(f"The {direction}d text is {text}")