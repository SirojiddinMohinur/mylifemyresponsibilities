'''import random
x=[]             #bu internetan olingan function yordamida yechilgan
y=[]
z=[]
for i in range(0,10):
    a=random.randrange(0,101)
    b=random.randrange(0,101)
    x.append(a)
    y.append(b)
def Intersectio(a1,b1):
    return set(a1).intersection(b1)
print(x,'\n',y)
print(Intersectio(x,y))'''


'''x=[]
y=[]
z=[]                                  #bu shaxshiy sodda usul
import random
for i in range(0,10):
    a=random.randrange(0,20)
    b=random.randrange(0,20)
    x.append(a)
    y.append(b)
for n in range(0,10):
    if x[n] in y: z.append(x[n])
print(x,'\n',y,'\n',z)'''

a=[1,23,45,22,2,4,5,322,7]  #listni set to`plamiga o`tkazamiz
b=[1,45,22,443,5,7,7]
a=set(a)
b=set(b)
z=a.intersection(b)         #intersection set to`plamida ishlaydi
z=list(z)                   # z ni listga o`tkazamiz
print(z)