ask=input('Difficult or simple password? (d/s) : ')
Table=[]
simple='abcdefghijklmnopqrstuvwxyz'
difficult='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

import random
if ask=='s':                                          # qiyin yoki oson parol yasash
    for i in range(4):
        a=random.choice(simple)
        Table.append(a)
    print('Simple password : ',''.join(Table))
else:
    for i in range(8):
        a=random.choice(difficult)
        Table.append(a)
    print('Difficult password : ',''.join(Table))

'''                         # funksiyaga olingan varianti
def Randompassword(ask):
    if ask=='s':
        for i in range(4):
            a=random.choice(simple)
            Table.append(a)
        print('Simple password : ',''.join(Table))
    else:
        for i in range(8):
            a=random.choice(difficult)
            Table.append(a)
        print('Difficult password : ',''.join(Table))

Randompassword(Ask)'''