string = input("Criminal: ")
##p = "`~!@#$%^&*()_+-=[]\{}|;':\",./<>?"
newstring=""
for letter in string:
    if letter.isalpha() or letter.isspace(): ##Obviously we want to get rid of space, but do we preserve it here so we can do .split()?
        newstring = newstring+letter
newstring=newstring.split()
output=""
for word in newstring:
    if len(word)>1:
        output=output+word

print(output)

