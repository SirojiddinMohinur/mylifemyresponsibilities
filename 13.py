#Fibonachi sonlar ya'ni son o`zidan oldingi ikki son yig`indisidan tashkil topadi
Element=int(input('Nechta fibonachi son ekranga chiqishini xohlaysiz? : '))
Fjadval=[1,1]

def funcFib(a):             # keyingi fibonachi son yasovchi funksiya
    uchinchi=a[-1]+a[-2]
    a.append(uchinchi)

for i in range(Element):    # fibonachilarni hisoblab jadvalga yozish
    funcFib(Fjadval)

print(Fjadval[:Element])    # kiritilgan songacha ekranga chiqarish


