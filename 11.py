#Created on Thu Aug 25 08:38:46 2022
a=int(input('Tub sonlikka tekshirish = '))
check=True
for i in range(2,a):
    if a%i==0:
        check=False
        break
if check==False: print('Tubmas')
else: print('Tub')
