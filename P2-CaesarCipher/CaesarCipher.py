import CaesarCipher_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
#            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Caesar Cipher Function
def CaesarCipher(command, plainText, shiftAmount):
    newText = ""

    for character in plainText:
        if character in alphabet:
            position = alphabet.index(character)

            if command == "encode":
                newPosition = position + shiftAmount
                if newPosition > 25:
                    offset = newPosition - 25
                    newPosition = offset - 1
            elif command == "decode":
                newPosition = position - shiftAmount
                if newPosition < 0:
                    offset = 25 + newPosition
                    newPosition = offset + 1
        
        
            newLetter = alphabet[newPosition]
            newText = newText + newLetter
        else:
            newText = newText + character   # if space or symbol is detected, it will just add to text without any operation

    
    print(f"message: {newText}")


# Main Program
print(CaesarCipher_art.logo)

flagAgain = True

while flagAgain:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n>>> ")

    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n>>> ")

        shift = int(input("Type the shift number:\n>>> "))
        if shift == 26:  # if big shift number is used
            shift = 1
        elif shift > 26:
            shift = shift % 26

        CaesarCipher(command=direction, plainText=text, shiftAmount=shift)
    else:
        print("Please enter the correct command: 'encode' or 'decode'")

    runAgain = input("Do you want to run again? [y/n]\n>>> ")
    if runAgain == 'y':
        flagAgain = True
    else:
        flagAgain = False
        print("Program Terminated!")
    print()
