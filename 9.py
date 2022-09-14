print('Men son o`ylayman sen topasan!')
import random
s=0
a=random.randrange(1,9)
print('o`ylangan son=',a)
while True:
    tahmin=int(input('Tahminingni kirit = '))
    if tahmin>a: print('                            Kotta son ettiz')
    elif tahmin<a: print('                           Kichkinayu bu son\n')
    s+=1
    if tahmin==a:
        print('                             Wow toptizu')
        print('Urunishlar soni= ', s)
        if input('Yana o`ynismi? (ha,yoq)')=='ha':
            a = random.randrange(1, 9)
            print('o`ylangan son=', a)
            s=0
        else:   break
