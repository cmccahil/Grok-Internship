##repeatedLettersDecoder

string = input("Message: ")
output=""

count=0
directionLetters=['R','L','S','W']
for letter in string:
    if letter.isdigit():
        count=(count*10)+int(letter)
    elif count>0:
        output=output+(letter*count)
        count=0
    else:
        output=output+letter

for m in output:
    if m in directionLetters:
        if m == 'R':
            print("Turn Right")
        elif m == 'L':
            print("Turn Left")
        elif m == 'S':
            print("Go Straight")
        elif m== 'W':
            print("Arrive at Warehouse")
            break

    
        
