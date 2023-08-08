# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 20:43:55 2023

@author: xudoy
"""

#LUG'AT ICHIDA LUG'AT

#dasturchilar={
#    'ali':['python',  'c++'],
    #'vali':['html',  'css',  'js'],
   # 'hasan':['php',  'sql'],
   # 'husan':['python',  'php'],
   # 'maryam':['c++',  'c#']
  #  }
#for ism,tillar in dasturchilar.items():
#    print(f"\n{ism.title()}:",end='')
#    for til in tillar:
#        print(f'{til.upper()}',end='')
        
        
#LUG'AT ICHIDA LUG'AT
#hamkasblar={
#    'ali':{'familiya':'valiyev',
#           'tyil':1995,
#           'malumot':'oliy',
#           'tillar':['python','c++']},
    
#    'vali':{'familiya':'aliyev',
#            'tyil':2001 ,
#            'malumot':"o'rta maxsus",
#            'tillar':['html','css','js']},
    
#    'hasan':{'familiya':'husanov',
#             'tyil':1999,
#             'malumot':'maxsus',
#             'tillar':['pyhton','php']}}
#for ism,info in hamkasblar.items():
#    print(f"\n{ism.title()} {info['familiya'].title()},"
#          f"{info['tyil']}-yilda tug'ilgan. \n"
#          f"Ma'lumoti: {info['malumot']}.\n"
#          "Quyidagi dasturlash tilllarini biladi:")
#for til in info['tillar']:
 #   print(til.upper())

# AMALIYOT
#mashhurlar={
#    'leonardo di caprio':["americada tug'ilgan aktyor.Titanic va boshqalarda bosh rol ijrochisi"],
#    'elvs presley':['rock yulduzi', 'oscar sohibi', 'grammy sohibi' ],
#    'c ronaldo':['38 yosh portugaliyada tavallud topgan futbolchi'],
#    'zaha hadid':['lvianda tugilgan arxitektor'],
#    'eynshteyn':['fizikadan nobel sohibi']}
#for ism, tariflar in mashhurlar.items():
#    print(f"\n{ism.title()}:",end='')
#    for tarif in tariflar:
#        print(f'{tarif.upper()}',end='')



#print('space space space space space')


#nasaf={
#       'shuxrat muhammadiyev':['yarim himoyachi 27 yoshda'],
#       'qobil berdiyev':['darvozabon 22 yoshda osiyo chempioni'],
#       'ruziqul berdiyev':['murabbiy 50 yoshda'],
#       'javohir karimov':['himoyachi 25 yoshda'],
#       'ravshan ermatov':['fifa referesi 48 yoshda'],
#       }

#for ism,ishtirokchilar in nasaf.items():
#    print(f"\n{ism.title()}:", end='')
#    for ishtirokchi in ishtirokchilar:
#        print(f'{ishtirokchi.upper()}', end='')

#print('space space space space space')


#cars={
#      'bmw':['germaniyada ishlab chiqarilgan. X7 mashhur yoltanlamasi'],
#      'toyota':['yapon avtomobil ishlab chiqaruvchisi. Camry rusumi mashhur'],
#      'chevrolet':['amerika avtocompaniyasi va tahoe mashhur rusumi'],
#      'range rover':['ingliz mashinasi va Range rover sport eng masghur'],
#      'mercedes':['nemis mashinasi va Gelendwagen juda mashhur']}
#for rusum, mashinalar in cars.items():
#    print(f"\n{rusum.title()}:", end='')
#    for mashina in mashinalar:
#        print(f'{mashina.upper()}',end='')

#print('space space space space')

#laptops={
 #   'hp':['amerika brendi pavilion mashhur rusumi'],
 #   'lg':['Janubiy koreya brendi hammasiyaxshi ishlasa kerak'],
  #  'samsung':['janubiy koreya brendi hamma laptoplari mashhur'],
  #  'apple':['amerika brendi mackbook eng mashhur mahsuloti']}
#for rusumi,laptop in laptops.items():
#    print(f"\n{rusumi.title()}:",end='')
 #   for komp in laptop:
 #       print(f'{komp.upper()}:',end='')




#oshnalar={
#    'xumoyun':['action kinolar ishqibozi'],
#    'zayniddin':['kino tomosha qilib uxlab qoladi'],
#    'lazizbek':['tarixiy yoki hujjatli filmlar muhlisi']}
#for oshna, kinolar in oshnalar.items():
#    print(f"\n{oshna.title()}:",end='')
#    for kino in kinolar:
#        print(f'{kino.upper()}',end='')
    


#davlatlar={
#    'aqsh':['shimoliy qutbda joylashgan dunyodagi eng qudratli davlat'],
#    'hindiston':['dunyoning eng kop aholiga ega davlati'],
#    'uzbekiston':['dunyoning eng korrupsion davlatlaridan biri'],
#    'rossiya':['hududi boyicha eng katta davlat']}
#for davlat, xususiyatlar in davlatlar.items():
#    print(f"\n{davlat.title()}:",end='')
#    for xususiyat in xususiyatlar:
#        print(f'{xususiyat.upper()}',end='')



#davlatlar = {
#    "o'zbekiston":{'poytaxt':"toshkent",
#                   'maydon':448978,
#                   'aholi':33_000_000,
#                   'pul birligi':"so'm"
 #                  },
#    "rossiya":{'poytaxt':"moskva",
#                   'maydon':17_098_246,
#                   'aholi':144_000_000,
#                   'pul birligi':"rubl"
#                   },
#    "aqsh":{'poytaxt':"vashington",
#                   'maydon':9_631_418,
#                   'aholi':327_000_000,
#                   'pul birligi':"dollar"},
#    "malayziya":{'poytaxt':"kuala-lumpur",
#                   'maydon':329750,
#                   'aholi':25_000_000,
#                   'pul birligi':"rinngit"}
#    }

#davlat = input('Davlat nomini kiriting: ').lower()
#if davlat in davlatlar:
#    info = davlatlar[davlat]
#    print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
#          f"\nHududi: {info['maydon']} kv.km"
#          f"\nAholisi: {info['aholi']}"
#          f"\nPul birligi: {info['pul birligi']}")
#else:
#    print("Bizda bu davlat haqida ma'lumot mavjud emas")
    
        
#mamlakatlar={
#    "gruziya":{'poytaxt':"yerevan",
#               'maydoni':69700,
#               'aholisi':3_709_000,
#               'pul birligi':'lari',
#           },   
#    'angliya':{'poytaxt':'london',
#               'maydoni':130279,
#               'aholisi':180_000_000,
#               'pul birligi':'pound sterling',
#               },
#    'indonesia':{'poytaxt':'jakarda',
#                 'maydoni':1904569,
#                 'aholisi':273_800_000,
#                 'pul birligi':'indoneziya rupisi'
#                 },
#   'canada':{'poytaxt':'ottawa',
 #            'maydoni':9093507,
 #            'aholisi':38_250_000,
 #            'pul birligi':'canada dollari'}
 #     } 
#mamlakat=input('Mamlakat nomini kiriting : ').lower()
#if mamlakat in mamlakatlar:
#    info=mamlakatlar[mamlakat]
#    print(f"\n{mamlakat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
#          f"\nHududi: {info['maydoni']} kv.km"
#          f"\nAholisi:{info['aholisi']}"
#          f"\nPul birligi:{info['pul birligi']}")
#else:
#        print("Bunday davlat mavjud emas")




cars={
      'mercedes':{'founder':'carl benz',
                  'country':'germany',
                  'income':'5 billion',
                  'types':'gls, g63, maybach'},
      'porsche':{'founder':'marc hamilton',
                 'country':'germany',
                 'income':'6 billion',
                 'types':'carrera, cayenne, panamera'
                 },
      'lamborghini':{'founder':'ferucco lamborghini',
                     'country':'italy',
                     'income':'8 billion',
                     'types':'urus,aventador,huracan'
                     },
      'chevrolet':{'founder':'jack blome',
                   'country':'usa',
                   'income':'7 billion',
                   'types':'camaro, tahoe, suburban'}}

car=input('Enter the car name : ').lower()
if car in cars:
    info=cars[car]
    print(f"\n{car.capitalize()} of founder is {info['founder'].title()}"
          f"\nCountry:{info['country']}"
          f"\nIncome:{info['income']}"
          f"\nmodels:{info['types']}"
          )
else:
      print("This car is not found")  
























































