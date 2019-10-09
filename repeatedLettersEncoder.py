##repeatedLettersEncoder

string=input("Message: ")
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
print(output)
        
        
