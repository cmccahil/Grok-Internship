topwords=[]
with open('TopWords.txt') as f:
   for line in f:
      topwords.append(line.strip())
print(topwords)
