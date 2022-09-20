menu={
    'Osh':'20000',
    'Sho`rva':'16000',
    'Lag`mon':'18000',
    'Norin':'18000',
    'Tovuq dimlama':'22000',
    'Mastava':'15000'}
tabmeals=[]
print('3 ta taom kiriting. ')
for ask in range(1,4):
    meal=input(f'{ask} chi taom > ')
    tabmeals.append(meal.capitalize())
print('Menuda bor taomlar.', tabmeals)
for check in tabmeals:
    if check in menu:
        print(f'{check} {menu[check]} so`m')
    else: print(f'Bizda {check} yo`q')


