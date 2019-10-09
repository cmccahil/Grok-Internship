#repeatedLettersDecoder(2)

string = input("Message: ")
output=""
previousDigit=""
for letter in string:
    if letter.isdigit():
        previousDigit=previousDigit+letter
    elif previousDigit == "":
        output=output+letter
    else:
        output=output+(letter*int(previousDigit))
        previousDigit=""

print(output)

