# # # # def inf(name,data):
# # # #     #ism va tug`ilgan yilini chiqaruvchi
# # # #     print(f'Assalom alekum {name.title()}, siz {data}-yilda tug`ilganmisiz?')
# # # #
# # # # ism=input('Ismingizni kiriting: ')
# # # # yosh=int(input('Tug`ilgan yilingizni kiriting: '))
# # # # inf(ism,yosh)
# # # # '''check=input(f'{ism.title()} siz haqiqatda {yosh}-yilda tug`ilganmisiz (ha/yo`q): ')
# # # # if check.lower()=='ha': print(f'{2022-yosh} yoshga to`libsizku.')'''
# # # number=int(input('Enter number: '))
# # # def check(a):
# # #     for i in range(2,11):
# # #         if a%i==0: print(f'{a} soni {i} soniga qoldiqsiz bo`linadi')
# # # check(number)
# #
# # a,b=9,8
# # def sqr(qiymat): #a ning kvadrat qiymatini qaytaruvchi funksiya
# #     qiymat=qiymat**2
# #     return qiymat
# # new=sqr(a)
# # math=new+8*b
# # math1=new-11
# # print(math,math1)
#
# #Lug`at yasidgan funksiya
#
# print('Smartfonlar haqidagi ma`lumotlarni to`plovchi dastur')
# Tel=[]
# def telefonlar(company,model,HDD,RAM):
#     SmartPhone={
#         'Kompaniyasi':company,
#         'Modeli':model,
#         'Doimiy xotirasi':HDD,
#         'Tezkor xotirasi':RAM     }
#     return SmartPhone
# comp=input('Kompaniyasi: ')
# mod=input('Modeli: ')
# xot=input('Xotira hajmi: ')
# ozu=input('RAM xotirasi: ')
# Tel.append(telefonlar(comp,mod,xot,ozu))
# print(Tel)
#
