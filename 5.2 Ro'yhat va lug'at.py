# -*- coding: utf-8 -*-
"""
Created on Tue May 16 21:20:34 2023

@author: xudoy
"""
#mahsulotlar={
 #   'olma':10000,
 #   'uzum':5000,
#    'shokolad':2000}
#bozorlik=['anor','uzum','non','shaftoli','uzum']
#for m in mahsulotlar:
#    if m in bozorlik:    
#        print(f"{m.title()} {mahsulotlar[m]} so'm")



#cars={
#      'bmw':45000,
#      'audi:':30000,
#      'chevrolet':50000,
#      'kia':35000}
#tanlov=['bmw','toyota','chevrolet','nissan','honda']
#for m in cars:
#    if m in tanlov:
#        print(f"{m.title()} {cars[m]} so'm")

#mahsulotlar={
#    'olma':5000,
#    'banan':6000,
#    'olxo\'ri':3000,
#    'anjir':5000,
#    'uzum':7000
#    }
#print(mahsulotlar.keys())
#print('Do\'kondagi mahsulotlar')
#for mahsulot in mahsulotlar.keys():
#    print(mahsulotlar.title())
#bozorlik=['olma','banan','anjir']
#for m in mahsulotlar:
#    if m in bozorlik:
#        print(f"{m.title()} {mahsulotlar[m]} so'm ")



#kutubxona={
#    'roman':200,
#    'biografiya':35,
#    'tarixiy':147,
#    'she\'rlar':400,
#    'qissalar':562,
#    'hikoyalar':612,
#    'maqolalar':500,
#    'ilmiy asarlar':84
#    }
#print(kutubxona.keys())
#print('Do\'kondagi mahsulorlar')
#for book in kutubxona.keys():
#    print(book.title())

#kitob=['roman','qissalar','she\'rlar','feletonlar','epizodlar','balladalar']
#for order in kutubxona:
#   if order in kitob:
 #       print(f"{order.title()} soni {kutubxona[order]} adadda")
#        for order in kutubxona:
#             if order not in kitob:
#                print(f"kechrasiz bizda {order} kitobi mavjud emas ")


# Lug'at elementlerini tartib bilan chiqarish



#mahsulotlar={'olma':5000,
#             'anor':6000,
#             'uzum':4000,
#             'olxo\'ri':7000,
#             'shafftoli':10000,
#             'banan':7000
#             }
#mahsulot=['uzum','kivi','anor','behi','limon','banan']
#print("Do'konimizdagi mahsulotlar:")
#for mahsulot in sorted(mahsulotlar):
#    print(mahsulot.title())
#cars={
#      'matiz':5000,
#      'mercedes':25000,
#      'lacetti':10000,
#      'damas':9000,
#      'porsche':65000,
#      'audi':56000,
#      'toyota':40000,
#      'honda':42000}
#car=['toyota','mercedes','damas','spark','cruze','porsche']
#print("Do'konimizdagi avtomobillar :")
#for car in sorted(cars):
#    print(car.title())


#.values() metodi

#telefonlar={
#    'ali':'iphone x',
#    'vali':'galaxy s9',
#    'olim':'mi 10',
#    'orif':'nokia 3310'}
#print(telefonlar.values())
#print('Fydalanuvchilarning telefonlari :')
#for tel in telefonlar.values():
#    print(tel)


#telefonlar={
#    'ali':'iphone x',
#    'vali':'galaxy s9',
#    'olim':'mi 10',
#    'orif':'nokia 3310',
#    'aziz':'iphone x',
#    'bek':'galaxy s9',
#    'alan':'mi 8',
#    'daler':'iphone x',
#    'ozoda':'galaxy s9'}
#print(telefonlar.values())
#print('Foydalanuvchilarning telefonlari :')
#for tel in set(telefonlar.values()):
#    print(tel)


#Amaliyot
#lugat={'set':'kalit va qiymatlarni alifbo tartibida chiqaradi',
#       'for':'tarmoqlanish siklli funksiya',
#       'upper':'qiymatni faqat bosh harfda chiqaradi',
#       'title':'qiymatni faqat birinchi harfini katta harfda beradi',
#       'or':'shart funksiyasida yoki shartini bajaradi',
#       'and':'shart funksiyasida va shartini bajaradi',
#       'print':'chop etish funksiyasini bajaradi',
#       'keys':'kalit so\'zni bildiradi',
#       'values':'berilgan kalit so\'zning qiymatini bildiradi',
#       'true':'qiymatning to\'riligini aniqlaydi',
#       'false':'qiymatning yolg\'onligini aniqlaydi'}
#print("Python lug'ati bilan tanishing :")
#for lugat1 in sorted(lugat.keys()):
#    print(lugat1)
#for lugat1 in sorted(lugat.values()):
#    print(lugat1)

#davlatlar={'gruziya':'tbilisi',
#           'armaniston':'erevan',
#           'afg\'oniston':'kobul',
#           'o\'zbekiston':'toshkent',
#           'aqsh':'washington',
#           'pokiston':'islomobod',
#           'qozog\'iston':'ostona',
#           'italiya':'rim',
#           'germaniya':'berlin',
#           'fransiya':'parij',
#           'belgiya':'bryussel',
#           'chexiya':'praga',
#           'ruminiya':'budapesht'
#           }
#print(sorted(davlatlar.keys()))
#print("Davlatlar va ularning poytaxtlari ")
#davlat=input("Biror davlat nomini kiriting : ")
#print(davlatlar.get(davlat, "Bunday ma'lumot mavjud emas"))
#poytaxt=davlatlar.get(davlat)
#if poytaxt==None:
#    print("Kechirasiz bizda bunday ma'lumot yo'q") 
#else:
#    print(f"{davlat}ning poytahti {poytaxt} shahri")




#products={'apple':'olma',
#          'lime':'limon',
#          'banana':'banan',
#          'meat':'gosht',
#          'carrot':'sabzi',
#          'bean':'loviya',
#          'onion':'piyoz'}

#kalit=input("Kalit so'zni kiriting : ")
#print(products.get(kalit, "Bunday so'z mavjud emas"))
#tarjima=products.get(kalit)
#if tarjima==None:
#    print("Bunday so'z mavjud emas")
#else:
#    print(f"{kalit} {tarjima} deb trjima qilinadi")

#davlatlar = {
#    "o'zbekiston":'toshkent',
 #   'aqsh':'washington d.c.',
 #   'rossiya':'moskva',
  #  'tojikiston':'dushanbe',
  #  "qirg'iziston":'bishkek',
 #   'qozog\'iston':'nursulton',
 #   'malayziya':'kuala-lumpur',
 #   'singapur':'sungapur',
 #   'italiya':'rim'}

#print('Dunyo davlatlari:')
#for davlat in sorted(davlatlar):
#    print(davlat.upper())


#print('\nDavlatlarning poytaxtlari')
#for poytaxt in sorted(davlatlar.values()):
 #   print(poytaxt.title())

#country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
#capital = davlatlar.get(country)
#if capital==None:
 #   print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
#else:
#    print(f"{country.upper()}ning poytaxti {capital.title()} shahri")

#MENYU

#menu = {
#        'osh':20000,
 #       "lag'mon":22000,
#        'non':4000,
#        'choy':5000,
#        'shashlik':12000,
#        'somsa':6000,
#        'tabaka':15000
#        }

#print('3 ta taom buyurtma bering :')
#buyurtmalar = []
#for n in range(3):
#    buyurtmalar.append(input(f"{n+1}-taom:").lower())

#for buyurtma in buyurtmalar:
#    if buyurtma in menu:
#        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
#    else:
#        print(f"Kechirasiz, bizda {buyurtma} yo'q.")



#cars={
#      'bmw':15000,
#      'nexia':8000,
#      'volvo':19000,
#      'toyota':19000}

#print('3 ta avtomobil turini tanlang :')
#orders=[]
#for n in range(3):
#    orders.append(input(f"{n+1} car :").lower())

#for order in orders:
#    if order in cars:
#      print(f"{order.title()} {cars[order]} so'm")
#else: 
#      print(f"Kechirasiz bizda {order} yo'q")

#telefonlar={
#    'iphone':1400,
#    'samsung':1300,
#    'sony':1450,
#    'google':800,
#    'lg':680,
#    'nokia':800,
#    'artel':500
#    }
#print('3 ta telefon turini kiriting :')
#orders=[]
#for n in range(3):
#    orders.append(input(f"{n+1} telefon :").lower())

#for order in orders:
#    if order in telefonlar:
#        print(f"{order.title()} {telefonlar[order]} so'm")
#    else:
#        print("Kechirasiz bizda {order} yo'q")



laptops={
    'hp':800,
    'mac':2000,
    'lg':500,
    'msi':900,
    'asus':700,
    'acer':500
    }
print("3ta kompyuter turni kiriting :")
orders=[]
for n in range(2):
    orders.append(input(f"{n+1} kompyuter :").lower())

for order in orders:
    if order in laptops:
        print(f"{order.title()} {laptops[order]} so'm ")
    else:
        print(f"Kechirasiz bizda {order} yo'q")


























