#NumberSchemeDecoder

f=open('TopWords.txt')
topwords=[]
sentence=input("Message: ")
for line in f:
    topwords.append(line.strip())
sentence=sentence.split()
output=""
for word in sentence:
    if word.isdigit():
        output=output+topwords[int(word)]+" "
    else:
        output=output+word+" "
print(output[0:-1])
