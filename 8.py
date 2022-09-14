
i=1
while i>0 :
    print("O`yindagi javoblar (tosh,qaychi,qog\'oz)")
    x = input('1-o`yinchi javobi=')
    y = input('2-o`yinchi javobi=')
    if (x=='tosh' and y=='qaychi'): print('G`olib 1-chi o`yinchi tabriklaymiz!!!')
    elif (x=="qaychi" and y=="qog'oz"): print('G`olib 1-chi o`yinchi tabriklaymiz!!!')
    elif (x=="qog'oz" and y=="tosh"): print('G`olib 1-chi o`yinchi tabriklaymiz!!!')
    else: print('G`olib 2-chi o`yinchi tabriklaymiz!!!')
    if input("Yana o`ynaysizmi?(ha,yo'q) :")=='ha': i+=1
    else:
        print('Tamom')
        break
