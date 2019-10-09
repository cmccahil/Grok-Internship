##repeatedLettersEncoder

string= "aaabccccaaahelloworldaaaa"
count=1
previousLetter=""
output=""
for letter in string:
    if letter == previousLetter:
        count+=1
    else:
        if count == 1:
            output=output+previousLetter
        else:
            output=output+str(count)+previousLetter
        count=1
        previousLetter=letter
if count == 1:
    output=output+previousLetter
else:
    output=output+str(count)+previousLetter
#print(output)
#repeatedLettersDecoder

string = output
output= ""

count=0
for letter in string:
    if letter.isdigit():
        count=(count*10)+int(letter)
    elif count>0:
        output=output+(letter*count)
        count=0
    else:
        output=output+letter

print(output)
