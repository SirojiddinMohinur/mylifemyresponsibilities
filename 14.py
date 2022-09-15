asosiyJadval=[]

import random
for i in range(20): asosiyJadval.append(random.randrange(0,15))  # random jadval yasash 20 talik
print(asosiyJadval)

asosiyJadval=set(asosiyJadval)    # jadvalni setga almashtirildi
Nusxa=asosiyJadval.copy()         # setda copy ishlatildi bir xil elementlarni tashlab yuborish uchun
asosiyJadval=list(Nusxa)          # setdan jadlavga qayta o`tkazildi
print(asosiyJadval)