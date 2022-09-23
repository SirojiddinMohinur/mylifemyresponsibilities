# # # # # # # for count in range(1,6):
# # # # # # #     if count==5: print(count)
# # # # # # #     else: print(count, end=',')
# # # # # # # count=1
# # # # # # # while count<=5:
# # # # # # #      if count==5: print(count)
# # # # # # #      else: print(count, end='-')
# # # # # # #      count+=1
# # # # # # ask=''
# # # # # # print('if you want stop programm you need write "exit"')
# # # # # # while ask!='exit':
# # # # # #     ask=(input('Enter number: '))
# # # # # #     if ask!='exit': print('Square of the number: ',float(ask)**2)
# # # # # #
# # # # # savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# # # # # savol += "Musbat son kiriting "
# # # # # savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# # # # #
# # # # # while True:
# # # # #     qiymat = int(input(savol))
# # # # #     if qiymat<0:
# # # # #         continue
# # # # #     elif qiymat=='exit':
# # # # #         break
# # # # #     else:
# # # # #         ildiz = float(qiymat)**(0.5)
# # # # #         print(f"{qiymat} ning ildizi {ildiz} ga teng")
# # # # ismlar = []
# # # #
# # # # print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# # # # n=1 # ismlarni sanash uchun o'zgaruvchi
# # # # while True:
# # # #     savol = f"{n}-do'stingiz ismini kiriting:"
# # # #     ism = input(savol)
# # # #     ismlar.append(ism)
# # # #     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
# # # #     if javob =='ha':
# # # #         n+=1
# # # #         continue
# # # #     else:
# # # #         break
# # # new={}
# # # name=input('Enter name of your friend: ')
# # # age=int(input(f'How old is {name}? '))
# # # new[name]=age
# # # print(new)
# # cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
# # while 'nexia' in cars: # toki nexia cars ro'yxati ichida ekan...
# #     cars.remove('nexia') # nexia ni ro'yxatdan olib tashla
# # print(cars)
# talabalar = ['hasan', 'husan', 'olim', 'botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = baho
# print(baholangan_talabalar)
