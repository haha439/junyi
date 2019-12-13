
amount = int(input())
total = 0

for i in range(1, amount+1):
    if i % 15 == 0:
        total  += 1
    elif i % 3 != 0 and i % 5 != 0:
        total += 1
print(total)
        
