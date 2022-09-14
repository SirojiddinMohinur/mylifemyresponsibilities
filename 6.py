
a=list(input('Palindromlkka tekshirish so`zini kiriting: '))
b=[]
#palindromlikka jadvalga solib tekshirildi
print(a)
for i in range(len(a),0,-1):
    b+=a[i-1]
if a==b:print(b,'P ku xaxaxaxa')
else: print(b,'P masu xaxaxaxa')