#NumberSchemeEncoder

f=open('TopWords.txt')
topwords=[]
sentence= input("Message: ")
for line in f:
    topwords.append(line.strip())
newstring=""
for letter in sentence:
    if letter.isalpha() or letter.isspace() or letter == "'":
        newstring=newstring+letter
newstring=newstring.split()
output=""
for word in newstring:
    if word in topwords:
        output=output+str(topwords.index(word))+" "
    else:
        output=output+word+" "
output=output[0:len(output)-1]
print(output)


