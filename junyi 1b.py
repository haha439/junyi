

sentence=input()
sentence = sentence.split()

sentencechange=str()
for i in range(len(sentence)-1):
    wordchange=str()
    for j in range(len(sentence[i])):
        wordchange += sentence[i][len(sentence[i])-j-1]
    sentencechange += wordchange
    sentencechange += " "

for j in range(len(sentence[-1])):
    wordchange = str()
    wordchange += sentence[-1][len(sentence[-1])-j-1]
    sentencechange += wordchange

print(sentencechange)
    