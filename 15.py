matn=input('Matn kiriting: ')

Jadvalmatn=matn.split()     # matn so`zlarini jadvalga oladi
print(matn)
                            # matn=' '.join(Jadvalmatn[::-1]) bunda reverse kerak bo`lmaydi
Jadvalmatn.reverse()        # jadval elementlarini teskarilaydi
print(Jadvalmatn)

matn=' '.join(Jadvalmatn)   # jadval elementlarini keltirilgan belgi asosida matnga oladi
print(matn)



