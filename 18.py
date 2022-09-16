import random

Usernumber = list(input('Enter your guessed number: '))
randomtable = []
cow = 0
bull = 0

for i in range(4):
    b = random.randrange(10)
    randomtable.append(b)

print(randomtable, ' ', Usernumber)
for ii in range(4):
    if int(Usernumber[ii]) == randomtable[ii]:
        cow += 1
    elif int(Usernumber[ii]) in randomtable:
        bull += 1
print('\nCow:', cow, ' Bull:', bull)
