

word=input()

wordchange=str()
for i in range(len(word)):
    wordchange += word[len(word)-i-1]
print(wordchange)
