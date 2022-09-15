a = []
c = []
n = int(input('Jadval elementlari sonini kiriting = '))
for i in range(n):
    a.append(input(f'Jadvalning {i + 1}-elementni kiriting: '))
print('a =', a)

def boshi_oxiri(b):  # b jadvalni birinchi va oxirgi elementini c jadvalga yozadi
    c.append(b[0])
    c.append(b[-1])
    print('c =', c)

boshi_oxiri(a)
