# #Creating list of purchasing products
# box=[]
# count=1
# print('Sotib olmoqchi bo`lgan mahsulotlaringiz ro`yxatini tuzamiz.'
#       '\n Barcha mahsulotlarni kiritganingizdan so`ng "exit" deb yozing')
# while True:
#     product=input(f'{count}-mahsulot: ')
#     if product.lower() == 'exit': break
#     box.append(product)
#     count+=1
# print(box)
# #Creating new market
# ecomarket={
#     'olma': 8000,
#     'anor': 10000,
#     'shampun': 25000,
#     'sovun': 9000,
#     'non': 2500,
#     'fanta': 12000
#     }
# while box:
#     product=box.pop()
#     if product in ecomarket.keys():
#         print(f'{product}ning narxi {ecomarket[product]} so`m')
