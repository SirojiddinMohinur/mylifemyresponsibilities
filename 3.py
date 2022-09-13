#5 dan kichkina sonlani jadvalga yig`adi
y=[]
x=[]
s=int(input('Nechta son kiritasiz = '))
for i in range(1,s+1):
    a=input(f'{i} - son = ')
    y.append(a)
    if int(y[i-1])<=5: x.append(y[i-1])

x.sort()
print(x)

