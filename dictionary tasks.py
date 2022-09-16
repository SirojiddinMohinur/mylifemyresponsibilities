otam=dict(ismi='Ziyoviddin', yoshi=48, kasbi='Shifokor')
onam=dict(ismi='Shaxnoza', shahar='Toshkent', kasbi='Shifokor')
ukalarim=dict(kasbi='Student', yoshlari='21,19,9')
print('otamning ismi',otam['ismi'],'yoshi',otam['yoshi'],'kasbi',otam['kasbi'])
print('onamning ismi',onam['ismi'],'tug`ilgan joyi',onam['shahar'],'kasbi',onam['kasbi'])
print('ular ',ukalarim['kasbi'],'yoshlari',ukalarim['yoshlari'])

Sevimli_taomlar={
    'nonushtaga':'Pizza, coffee',
    'tushlikga':'shashlik, sho`rva',
    'kechlikga':'osh,qozonkabob'
    }
print('\nBugungi Menu')
son=input('\nnonushtaga/tushlikga/kechlikga ?  :')
if son in Sevimli_taomlar : print(Sevimli_taomlar[f'{son}'])
else: print('So`zni noto`gri kiritdingiz')
