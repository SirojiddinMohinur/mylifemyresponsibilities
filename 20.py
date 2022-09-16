# Binar qidiruv amalga oshirilmoqda
# Binar qidiruvda son 2 ga bo`lish orqali tekshiriladi
from bisect import bisect_left

Jadval = []
for i in range(9999999):
    Jadval.append(i)
son = int(input('Tekshiriluvchi son: '))


def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1


tekshiruv = BinarySearch(Jadval, son)
print(tekshiruv)
